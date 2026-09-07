"""
Black-Scholes Option Pricer + Greeks
-------------------------------------
Based on: Black & Scholes (1973), Merton (1973)
Related GS Paper: "When You Cannot Hedge Continuously" (Kamal)

Usage:
    pricer = BlackScholes(S=100, K=105, T=0.5, r=0.05, sigma=0.2)
    print(pricer.call_price())
    print(pricer.greeks())
"""

import numpy as np
from scipy.stats import norm


class BlackScholes:
    def __init__(self, S: float, K: float, T: float, r: float, sigma: float):
        """
        S     : Current stock price
        K     : Strike price
        T     : Time to expiry in years (e.g. 0.5 = 6 months)
        r     : Risk-free interest rate (annualized, e.g. 0.05 = 5%)
        sigma : Volatility of the stock (annualized, e.g. 0.2 = 20%)
        """
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self._d1, self._d2 = self._compute_d()

    def _compute_d(self):
        """Compute d1 and d2 — the heart of Black-Scholes."""
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) \
             / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        return d1, d2

    def call_price(self) -> float:
        """Price of a European call option."""
        return (self.S * norm.cdf(self._d1)
                - self.K * np.exp(-self.r * self.T) * norm.cdf(self._d2))

    def put_price(self) -> float:
        """Price of a European put option (via put-call parity)."""
        return self.call_price() - self.S + self.K * np.exp(-self.r * self.T)

    def greeks(self) -> dict:
        """
        The Greeks — sensitivity measures for hedging.

        Delta  : How much the option price changes per $1 move in S
        Gamma  : How much Delta changes per $1 move in S (convexity)
        Vega   : How much the price changes per 1% move in volatility
        Theta  : How much the price decays per day (time decay)
        Rho    : How much the price changes per 1% move in interest rate
        """
        d1, d2 = self._d1, self._d2
        S, K, T, r, sigma = self.S, self.K, self.T, self.r, self.sigma

        delta_call = norm.cdf(d1)
        delta_put  = delta_call - 1
        gamma      = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        vega       = S * norm.pdf(d1) * np.sqrt(T) / 100          # per 1% vol move
        theta_call = (-(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
                      - r * K * np.exp(-r * T) * norm.cdf(d2)) / 365  # per day
        theta_put  = (-(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
                      + r * K * np.exp(-r * T) * norm.cdf(-d2)) / 365
        rho_call   = K * T * np.exp(-r * T) * norm.cdf(d2) / 100  # per 1% rate move
        rho_put    = -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100

        return {
            "call_price": round(self.call_price(), 4),
            "put_price":  round(self.put_price(), 4),
            "delta_call": round(delta_call, 4),
            "delta_put":  round(delta_put, 4),
            "gamma":      round(gamma, 4),
            "vega":       round(vega, 4),
            "theta_call": round(theta_call, 4),
            "theta_put":  round(theta_put, 4),
            "rho_call":   round(rho_call, 4),
            "rho_put":    round(rho_put, 4),
        }

    def implied_vol(self, market_price: float, option_type: str = "call",
                    tol: float = 1e-6, max_iter: int = 200) -> float:
        """
        Back out implied volatility from a market price using Newton-Raphson.
        This is what quants do every day — market prices imply a vol, not the other way.
        """
        sigma = 0.2  # initial guess
        for _ in range(max_iter):
            bs = BlackScholes(self.S, self.K, self.T, self.r, sigma)
            price = bs.call_price() if option_type == "call" else bs.put_price()
            vega  = bs.greeks()["vega"] * 100  # undo the /100 scaling
            diff  = price - market_price
            if abs(diff) < tol:
                return round(sigma, 6)
            sigma -= diff / vega
            sigma = max(1e-6, sigma)  # keep positive
        raise ValueError("Implied vol did not converge. Check inputs.")


# ── QUICK DEMO ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("Black-Scholes Pricer Demo")
    print("=" * 50)

    bs = BlackScholes(S=100, K=105, T=0.5, r=0.05, sigma=0.20)
    g  = bs.greeks()

    for k, v in g.items():
        print(f"  {k:<15}: {v}")

    print("\nImplied vol for call priced at $5.00:")
    iv = BlackScholes(S=100, K=105, T=0.5, r=0.05, sigma=0.2).implied_vol(5.0)
    print(f"  σ_implied = {iv:.4f} ({iv*100:.2f}%)")
