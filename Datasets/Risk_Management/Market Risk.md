## Capital Asset Pricing Model (CAPM):

- **Definition**: Formula to calculate expected return of a security based on its risk.
- **Components**: Considers risk-free rate, Beta (systematic risk), and market risk premium.
- **Formula**: CAPM = Risk-free rate + Beta × Market risk premium.
- **Interpretation of Beta**: Greater than 1 implies greater volatility; less than 1 implies less volatility.
- **Limiting Assumptions**: Includes transaction costs and taxes.

## Relationship with Efficient Frontier:

- **CAPM vs. Efficient Frontier**: CAPM considers risk-free rate, while the efficient frontier does not.
- **Capital Market Line (CML)**: Linear line starting at the risk-free rate.
- **Efficient Frontier**: Parabola representing combinations of risky assets. Also known as Markowitz bullet upward portion 
- **Efficient Portfolio**: Intersection of CML and efficient frontier, considered the market portfolio.
- **Utilization**: CAPM and efficient frontier used together to determine the most efficient portfolio.

## Application in Financial Risk Management:

- **Capital Market Theory**: Utilized within financial risk management, incorporating concepts like CML and security market line.
- **Importance of Risk-Free Rate**: CML and security market line consider the risk-free rate, unlike the efficient frontier.
- **Efficiency of Portfolio**: Combination of efficient frontier and CML aids in identifying the most efficient portfolio.
## Market Risk: Framework & Strategies

### Financial Instruments

> Financial instruments, including bonds, stocks, and derivatives, are key sources of market risk, which arises from price changes in these assets. Bonds and stocks represent fixed-income and equity securities, while derivatives, such as futures, can be used to hedge and manage portfolio risks. Understanding these instruments and their price movements is essential for effective market risk measurement and management.
#### Bonds 
##### Bonds and Risk Management Summary  
The bond market is significantly larger than the stock market and is a key focus for institutional investors like pension funds. Risk managers analyze factors affecting bond prices, primarily interest rates and credit quality. Government bonds are mainly impacted by interest rate changes, while other fixed-income products, such as loans and mortgages, share similar risks.  

**Key Concepts:**  
- **Present Value & Pricing:** Bond prices are calculated by discounting expected cash flows at market interest rates. Bonds trade at par, premium, or discount depending on the relationship between coupon rates and yields.  
- **Price-Yield Relationship:** Bond prices and yields are inversely related, with price-yield curves demonstrating positive convexity. Duration estimates a bond's price sensitivity to interest rate changes, with higher duration indicating greater risk.  
- **Types of Bonds:** Bonds vary from fixed-coupon and zero-coupon bonds to inflation-protected securities and structured notes, each with unique features and risk profiles.  
- **Strategies:** Passive strategies focus on holding bonds to maturity, while active strategies include trading on valuation, interest rate forecasts, or leveraging derivatives like futures and swaps to manage risk or adjust duration.  

Effective bond management relies on understanding these principles to align risks with investment goals.  

#### Equities
##### Equities Overview
- Represent ownership of cash flows remaining after bondholders and creditors are paid.
- Riskier and harder to predict than bonds, making valuation challenging.

##### Risk Factors in Investments
- **Interest Rate Risk**: Changes in interest rates affect both bonds and equities.
- **Business Risk**: Depends on economic conditions affecting profits or losses.
- **Financial Risk (Leverage)**:
  - Involves borrowing to increase debt instead of issuing equity.
  - Measured by debt-to-equity or debt-to-asset ratios.
- **Systematic Risk**: 
  - Variability in equity prices due to market changes.
  - Measured by Beta.
- **Unsystematic Risk**:
  - Unique to a specific company.
  - Can be managed through diversification.

##### Measuring Equity Risk
- **Standard Deviation (Volatility)**: Measures overall risk.
- **Beta**: Indicates systematic risk or market risk.
- **Value at Risk (VaR)**: Probabilistic measure of potential losses

##### Capital Market Line (CML)
- Tangent from the risk-free rate to the efficient frontier at the market portfolio.
- Points along the CML provide better risk-return ratios than the efficient frontier.
- Market portfolio represents maximum diversification.

##### Risk in Portfolios
- **For Undiversified Portfolios**: Volatility is a key measure of potential losses.
- **For Diversified Portfolios**: Beta is a better risk measure.

##### Capital Market Theory (CAPM)
- **Portfolio Management**:
  - Higher Beta stocks have higher expected returns.
  - Diversification reduces risk; Beta measures remaining risk.
- **Risk Management**:
  - Beta reflects undiversifiable risk proportional to market covariance.
  - Beta of 1 equals market risk, scaling with market changes.

##### Optimal Investment Strategies
- Invest in a diversified market portfolio (e.g., S&P 500, MSCI World Index).
- Risk-averse investors: Allocate funds between the market portfolio and bonds (e.g., 60/40 strategy).
- Risk-tolerant investors: Use leverage (margin loans or borrowed funds) to scale risk.

##### Leverage in Investment
- Retail investors: Margin loans.
- Hedge funds: Borrow 2-10x their base capital to achieve higher returns and face greater losses.

#### Derivatives and Managing Market Risk

##### Derivatives Market Overview
- Derivatives: Value derived from assets (**stocks**, **bonds**, etc.).
- Types: OTC and exchange-traded.
- Used to hedge risks in portfolios (**bonds**, **equities**, **commodities**).
- Market size: $1,000 trillion.

##### Risk and Clearinghouses
- Counterparty risk: Cleared by clearinghouses.
- **Clearinghouses**: Net transactions, require collateral, liquidate positions if needed, maintain guarantee funds.
- Systemic risk: Clearinghouses centralize risk; may need central bank intervention.

##### Forward Contracts and Swaps
- **Forward**: Lock future prices (commodities).
- **Swaps**: Exchange cash flows (**interest rates**, **commodities**) with longer maturities than forwards.

##### Futures Contracts vs. Forwards
- **Futures**: Standardized, traded on exchanges, liquid, daily margin settlement.
- **Hedging**: Short hedge (protect bond portfolio from interest rate rise), long hedge (lock in future bond yields).

##### Options Overview
- **Options**: Right to buy/sell at set price before expiration.
  - Calls: Buy, Puts: Sell.
- **Moneyness**: In-the-money (intrinsic value), at-the-money (no profit), out-of-the-money (no value).
- Option premium: Cost to buy options.

##### Option Strategies
- **Covered Call**: Own stock, sell call to generate income, limits upside.
- **Protective Put**: Buy put to protect against declines, costs premium.

### Measuring and Analysing Market Risk

> Market risk is measured using probabilistic and statistical methods. Probabilistic measures assess uncertain outcomes, while random variables reflect past data with unpredictable future behavior, crucial for financial assets. Key concepts include probability distributions, density functions, and cumulative distributions. Statistical measures like correlation coefficients evaluate data relationships, and regression analysis, such as comparing stock returns to market indices, calculates a stock's beta, indicating its market sensitivity.
#### Probability of a Loss
##### Measuring and Analyzing Market Risk

- **Overview**: Discusses market risk from probabilistic and statistical perspectives, focusing on modeling asset prices and returns.
  
- **Key Concepts**:
  - **Risk Factors**: Equity prices, bond prices, foreign exchange rates, commodity prices, interest rates, and indexes.
  - **Probability Distribution Function (PDF)**: Measures likelihood of specific outcomes within a range (e.g., asset prices or returns).
  - **Cumulative Distribution Function (CDF)**: Accumulates the probability from the PDF, summing to 1.

##### Discrete vs Continuous Variables
- **Discrete Variables**: Countable outcomes, e.g., rolling dice.
- **Continuous Variables**: Measure continuous ranges like asset prices or returns.

##### Probability Distributions and Their Use
- **Normal Distribution**: Often assumed in financial modeling, but it’s symmetric and can extend to negative values.
  - **Log Normal Distribution**: Corrects the negative value issue by introducing a zero lower bound for asset prices.

##### Mathematical Insights
- **Probability and Density Functions**: The PDF and CDF are mathematically related (CDF is the integral of the PDF).
- **Risk Measurement**: Using these functions helps quantify the probability of losses and the magnitude of potential losses.

##### Assumptions in Financial Risk
- **Asset Price Modeling**: Typically assumes prices follow a log-normal distribution to avoid negative asset values.
- **Value at Risk (VaR)**: The calculation of potential losses at a specific confidence level, with adjustments for skewness and lower bounds in asset prices.  

#### Statistical Measures

###### Statistical Measures of Risk

- **Visual Summaries of Data**
  - Tools: Histograms, scatter plots.
  - **Purpose**: Spot outliers, trends, and distribution patterns.
  - **Outliers**: Important to identify as they can affect risk management.

- **Basic Summary Measures**
  - **Mean**: Expected value.
  - **Median**: Midpoint of distribution.
  - **Quantile**: Used in value at risk (VaR) calculations.
  - **Variance/Standard Deviation**: Measure dispersion but don't reflect skewness or kurtosis.

- **Higher Moments of Distributions**
  - **Skewness**: Measures asymmetry of the distribution.
    - Positive Skew: Skewed to the right (positive returns).
    - Negative Skew: Skewed to the left (negative returns).
  - **Kurtosis**: Measures the "tailedness" of the distribution.
    - **Mesokurtic**: Normal distribution (average tail).
    - **Leptokurtic**: Fat tails (higher extreme values).
    - **Platykurtic**: Thin tails (lower extreme values).

- **Covariance and Correlation**
  - **Covariance**: Joint variability of two variables.
  - **Correlation Coefficient**: Strength of relationship between variables.
    - Ranges from -1 (perfect negative) to +1 (perfect positive).
    - Zero indicates no relationship.

- **Time Series Data & Serial Autocorrelation**
  - Time series data often shows correlation with earlier observations.
  - **Serial Autocorrelation**: Correlation of asset price with its past values.

- **Linear Regression**
  - Purpose: Study relationship and forecast values between variables.
  - **Equation**: Y = A + B * X.
    - **A (Intercept)**: Y-intercept of the regression line.
    - **B (Slope)**: Change in Y for each unit change in X.
  - **Beta**: Measures stock's relationship to market (e.g., Apple vs. S&P 500).
  - **Confidence**: Standard error and T-test assess the reliability of Beta.

### Managing and Modelling Market Risk

> Key measures like Value at Risk (VaR) and Expected Shortfall (ES) are explored, with ES providing a more comprehensive view of risk, especially for extreme losses. It also covers complementary methods such as Scenario Analysis and Stress Testing, which assess risk under potential or extreme future conditions, offering a more realistic picture of market vulnerability. This holistic approach is used to handle real-world market risks effectively.

#### Market Risk Measurement Systems

##### Overview of Market Risk Management
- Understanding financial instruments and derivatives for risk hedging is essential.
- Risk managers use various methods to measure and analyze market risk, especially in institutions like banks, asset managers, and insurance companies.

##### Risk Measurement Evolution
- **Volatility and variance**: Initially used for risk measurement based on returns.
  - Problem: Difficult to translate into capital allocation.
- **Position-based measures**: E.g., Value at Risk (VaR), provide better capital allocation insights, including portfolio loss estimation over a set time horizon and confidence level.
- **Stress testing**: Evaluates losses under extreme market conditions, typically defined by regulators.

##### Types of Financial Risks
- **Market, credit, and operational risks**: Three main categories.
- Interaction between these risks can lead to broader financial crises.
#### Downside Risk Measures

##### Value at Risk
- **Definition**: Measures portfolio downside risk, summarizing potential loss not exceeded at a chosen confidence level.
##### Methods to Calculate VaR
- **Historical Method**:
  - Construct a histogram of daily returns from recent market data.
  - Analyze the distribution (e.g., log-normal) and summarize loss at a chosen confidence level.
- **Monte Carlo Simulation**:
  - Assume a distribution for portfolio risk factors.
  - Simulate portfolio returns using random samples, generating a terminal price distribution.
  - Derive VaR for a given confidence level and time horizon.

##### VaR Limitations
- Does not account for extreme losses beyond the VaR threshold.
- Subject to sampling variation and error.
- Dependent on:
  - **Confidence Level**: Higher levels (e.g., 99%) increase VaR.
  - **Time Horizon**: Longer horizons yield higher VaR (adjusted via square root scaling for independent, identically distributed returns).

##### Conditional Value at Risk (CVaR) / Expected Shortfall
- Measures **average loss** in the left tail beyond the VaR threshold.
- Calculated as the integral of the loss distribution from zero to the VaR cutoff, divided by the tail probability (e.g., 5% for 95% confidence).

##### Time Horizon and Liquidity Risks
- **Liquidity Horizon**: Time needed to sell assets when losses occur.
  - Illiquid assets (e.g., real estate, loans) require longer horizons, amplifying losses during market stress.
- Adjust VaR from one day to multiple days:
  - Multiply one-day VaR by the square root of the time horizon.

##### Backtesting VaR Models
- Ensures the frequency of losses exceeding VaR aligns with the confidence level.
  - Example: For 95% confidence, expect losses to exceed VaR ~5% of the time in backtests.

##### Regulatory Guidance: Basel Committee
- **Market Risk Charge**:
  1. 10 trading days (2 calendar weeks) time horizon.
  2. 99% confidence level.
  3. At least 1 year of historical data, updated quarterly.
- Convert one-day VaR to 10-day VaR:
  - Multiply by √10 for a 99% confidence level.


#### Stress Testing and Scenario Analysis
##### Stress Testing and Scenario Analysis
- **Purpose**: Supplements models like Value at Risk (VaR) by accounting for extreme but plausible adverse scenarios.
- **Definition**: Projects financial conditions under adverse scenarios with one or more risk factors. 
  - Scenarios are plausible and extreme but not inconceivable.
  - Evolved as a critical tool after the 2007-2008 financial crisis.

##### Importance of Stress Testing
- Identifies **tail risk**: Extreme losses in the left tail of a risk distribution.
- Informs the **risk appetite framework**: Helps set policies to ensure capital and liquidity can withstand severe conditions.
- Highlights **event risks**: Rare, unexpected risks with catastrophic impacts (e.g., policy changes, geopolitical risks, market disruptions).

##### Features of Stress Tests
- Increases volatilities and stresses correlations between asset categories.
- Aggregates results across portfolios to report overall risk exposure.
- Focuses on high-severity scenarios with fewer risk factors.

##### Scenario Analysis
- Evaluates plausible but unlikely future events, which may or may not have historical precedence.
- Identifies emerging and strategic risks.
- Uses systematic methods to create scenarios:
  - Historical scenarios (e.g., 1987 market crash, COVID-19 market sell-off).
  - Hypothetical scenarios: Imagining the worst-case outcomes for positions.

##### Reverse Stress Testing
- Required by regulators to identify scenarios leading to insolvency or bankruptcy.
- Assumes large, catastrophic losses to explore potential causes and impacts.

##### Design Considerations
- Identify appropriate risk drivers and ensure data quality.
- Consult business line managers and risk experts for expert opinions.
- Use methods like moving key variables individually or simulating specific historical events.

##### Goal
- Prepare firms to withstand extreme but plausible scenarios, mitigating the risks of illiquidity and insolvency.


