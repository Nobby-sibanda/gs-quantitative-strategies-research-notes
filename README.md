# Quantitative Finance Interview Prep
### Built on Goldman Sachs Quantitative Strategies Research Notes (Derman et al.)

> **Nobby Sibanda** · Aspiring Quantitative Analyst · Pace University  
> This repo combines classic GS research papers with structured interview prep, Python implementations, and daily practice questions.

---

## 📚 Reading Roadmap (Start Here)

The GS papers are dense. Read them in this order — easiest to hardest:

### Stage 1 — Foundations (Week 1–2)
| Paper | Key Concept | Why It Matters |
|---|---|---|
| Model Risk | Model limitations & assumptions | Every quant interview asks this |
| Understanding GER Contracts | FX derivatives basics | Good entry point |
| Pay-On-Exercise Options | Exotic options intro | Builds intuition |

### Stage 2 — Volatility Core (Week 3–5)
| Paper | Key Concept | Why It Matters |
|---|---|---|
| The Volatility Smile and Its Implied Tree | Implied vol surface | Core quant knowledge |
| Is the Volatility Skew Fair? | Skew pricing | Common interview topic |
| Regimes of Volatility | Vol regimes | Risk management |
| Investing in Volatility | Vol as an asset class | Portfolio quant roles |
| More Than You Ever Wanted To Know About Volatility Swaps | Var swaps, vol swaps | Derivatives desks |

### Stage 3 — Advanced Models (Week 6–8)
| Paper | Key Concept | Why It Matters |
|---|---|---|
| The Local Volatility Surface | Local vol model | Derivatives pricing |
| Stochastic Implied Trees | Stochastic vol | Advanced roles |
| Implied Trinomial Trees | Numerical methods | Implementation |
| Static Options Replication | Replication strategy | Structuring |

---

## 🎯 Interview Questions by Topic

### Probability & Statistics
1. What is the difference between a random walk and a Brownian motion?
2. If I flip a fair coin until I get heads, what is the expected number of flips? *(Answer: 2)*
3. You have 3 boxes: one with 2 gold coins, one with 2 silver, one with one of each. You pick a box and pull out a gold coin. What's the probability the other coin is also gold? *(Ans: 2/3)*
4. What is Ito's Lemma and why does it matter in finance?
5. What's the difference between correlation and covariance? When would you use each?
6. Explain the Central Limit Theorem in plain English. Why is it so important?
7. What is a martingale? Give a financial example.
8. What is Jensen's Inequality and why does it matter for options?

### Derivatives & Options Pricing
1. Derive the Black-Scholes formula from first principles (or explain each assumption).
2. What are the Greeks? Explain delta, gamma, vega, theta, and rho intuitively.
3. Why does implied volatility smile/skew exist if Black-Scholes assumes constant vol?
4. What is put-call parity? Derive it.
5. What is a volatility swap vs. a variance swap? Which is more common and why?
6. How do you price a barrier option? What numerical methods can you use?
7. What is local volatility vs. stochastic volatility? Name a model for each.
8. What does it mean to be delta-hedged? Are you truly risk-free?
9. Explain the concept of implied trinomial trees (from the Derman/Kani paper).
10. What is static replication? How does it differ from dynamic hedging?

### Stochastic Calculus
1. What is Geometric Brownian Motion? Write the SDE for a stock price.
2. Apply Ito's Lemma to f(S,t) = ln(S) where S follows GBM.
3. What is risk-neutral pricing? Why can we change the probability measure?
4. What is the Girsanov theorem and why is it useful?
5. What is a Feynman-Kac formula?

### Risk & Portfolio Theory
1. What is Value at Risk (VaR)? What are its limitations?
2. What is Expected Shortfall (CVaR) and why is it preferred over VaR?
3. What is the Sharpe Ratio? How do you annualize it?
4. Explain the Capital Asset Pricing Model (CAPM). What are its assumptions?
5. What is factor investing? Name 3 common equity factors.
6. What is model risk? (Directly from the Derman paper — know this cold)
7. What is the difference between historical and Monte Carlo simulation for VaR?

### Brainteasers (Common at Top Firms)
1. You're offered a game: flip a coin, heads = $2, tails = $0. How much would you pay to play? What if it doubles each time you flip heads?
2. A stock is at $100. It can go to $110 or $90 next period. Risk-free rate is 5%. Price a call option with strike $105.
3. How many piano tuners are there in Chicago?
4. You have 25 horses and can race 5 at a time. How many races to find the top 3? *(Ans: 7)*
5. A clock shows 3:15. What is the angle between the hands? *(Ans: 7.5°)*
6. Two trains 100 miles apart, traveling at 50 mph each. A bird flies at 100 mph between them. How far does the bird fly before they meet? *(Ans: 100 miles)*

---

## 🐍 Python Implementations

See the `/python/` folder for implementations of:
- `black_scholes.py` — Black-Scholes pricer + Greeks
- `monte_carlo_options.py` — Monte Carlo option pricing
- `binomial_tree.py` — CRR binomial tree
- `var_calculator.py` — Historical and parametric VaR
- `volatility_surface.py` — Implied vol surface from market prices
- `portfolio_optimizer.py` — Mean-variance optimization

---

## 📅 Daily Practice Schedule

Each day, pick ONE from each category:
- **Read**: One GS paper (start with Stage 1, 20–30 min)
- **Practice**: One interview question above (write it out, then check)
- **Code**: One Python implementation

On busy days, just do the interview question. Consistency > intensity.

---

## 🔗 Additional Resources

- [Derman's Blog](http://www.emanuelderman.com/) — Essays from the author of these papers
- [Paul Wilmott on Quantitative Finance](https://www.wilmott.com/) — Deep technical reference
- [QuantLib](https://www.quantlib.org/) — Open-source quant library in Python/C++
- [QuantStackExchange](https://quant.stackexchange.com/) — Community Q&A
- [Heard on the Street](https://www.amazon.com/dp/0970055234) — Classic quant interview book
- [A Practical Guide To Quantitative Finance Interviews](https://www.amazon.com/dp/1438236662) — Xinfeng Zhou's green book
- [MIT OpenCourseWare — Finance Theory](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/)

---

## 📈 Progress Tracker

Track your daily reading:

| Week | Paper Read | Interview Q Practiced | Python Coded | ✓ |
|---|---|---|---|---|
| Week 1 | Model Risk | Brownian Motion vs Random Walk | black_scholes.py | ☐ |
| Week 2 | GER Contracts | Put-Call Parity Derivation | binomial_tree.py | ☐ |
| Week 3 | Volatility Smile | What is implied vol? | volatility_surface.py | ☐ |
| Week 4 | Volatility Skew | Greeks intuition | monte_carlo_options.py | ☐ |
| Week 5 | Vol Swaps | Variance swap pricing | var_calculator.py | ☐ |
| Week 6 | Local Vol Surface | Local vs stochastic vol | portfolio_optimizer.py | ☐ |
| Week 7 | Stochastic Trees | Ito's Lemma derivation | — | ☐ |
| Week 8 | Static Replication | Static vs dynamic hedge | — | ☐ |
