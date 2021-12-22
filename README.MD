<h1 align="center">
  <br>
  PY-Stocks
  <br>
</h1>

<h4 align="center">A minimal stocks API wrapper of <a href="https://github.com/ranaroussi/yfinance" target="_blank">yfinance</a>.</h4>

<p align="center">
  <a href="#build">Build</a> •
  <a href="#endpoints">Endpoints</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

## Build

To clone and run this application, you'll need [Git](https://git-scm.com) and [Docker](https://www.docker.com/get-started) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/pinkahd/py-stocks

# Go into the repository
$ cd py-stocks

# Build the image
$ docker build . -t py-stocks

# Run the app
$ docker run -p 8000:8000 py-stocks
```

## Endpoints

### Download

The `/download/:symbol/:startDate/:endDate` endpoint takes a symbol and a start and end date

Params:

- `interval` default `1d`

Example command

```bash
curl localhost:8000/download/AAPL/2021-08-01/2021-08-03 | jq
```

JSON Response

```json
{
  "Open": {
    "1627862400000": 146.3600006104
  },
  "High": {
    "1627862400000": 146.9499969482
  },
  "Low": {
    "1627862400000": 145.25
  },
  "Close": {
    "1627862400000": 145.5200042725
  },
  "Adj Close": {
    "1627862400000": 145.3023071289
  },
  "Volume": {
    "1627862400000": 62880000
  }
}
```

### Info

The `/info/:symbol` endpoint takes a symbol and return company information and the current price.

Example command:

```bash
curl localhost:8000/info/AAPL | jq
```

JSON Response:

```json
{
  "52WeekChange": 0.18871057,
  "SandP52WeekChange": 0.2816925,
  "address1": "One Apple Park Way",
  "algorithm": null,
  "annualHoldingsTurnover": null,
  "annualReportExpenseRatio": null,
  "ask": 0,
  "askSize": 1800,
  "averageDailyVolume10Day": 70456128,
  "averageVolume": 77309822,
  "averageVolume10days": 70456128,
  "beta": 1.202797,
  "beta3Year": null,
  "bid": 0,
  "bidSize": 1200,
  "bookValue": 3.882,
  "category": null,
  "circulatingSupply": null,
  "city": "Cupertino",
  "companyOfficers": [],
  "country": "United States",
  "currency": "USD",
  "currentPrice": 147.54,
  "currentRatio": 1.062,
  "dateShortInterest": 1628812800,
  "dayHigh": 149.12,
  "dayLow": 147.51,
  "debtToEquity": 210.782,
  "dividendRate": 0.88,
  "dividendYield": 0.006,
  "earningsGrowth": 1,
  "earningsQuarterlyGrowth": 0.932,
  "ebitda": 110934999040,
  "ebitdaMargins": 0.31955,
  "enterpriseToEbitda": 22.65,
  "enterpriseToRevenue": 7.238,
  "enterpriseValue": 2512655745024,
  "exDividendDate": 1628208000,
  "exchange": "NMS",
  "exchangeTimezoneName": "America/New_York",
  "exchangeTimezoneShortName": "EDT",
  "expireDate": null,
  "fiftyDayAverage": 146.94086,
  "fiftyTwoWeekHigh": 151.68,
  "fiftyTwoWeekLow": 103.1,
  "financialCurrency": "USD",
  "fiveYearAverageReturn": null,
  "fiveYearAvgDividendYield": 1.29,
  "floatShares": 16513305231,
  "forwardEps": 5.67,
  "forwardPE": 26.021162,
  "freeCashflow": 80625876992,
  "fromCurrency": null,
  "fullTimeEmployees": 147000,
  "fundFamily": null,
  "fundInceptionDate": null,
  "gmtOffSetMilliseconds": "-14400000",
  "grossMargins": 0.41005,
  "grossProfits": 104956000000,
  "heldPercentInsiders": 0.00071000005,
  "heldPercentInstitutions": 0.58426,
  "impliedSharesOutstanding": null,
  "industry": "Consumer Electronics",
  "isEsgPopulated": false,
  "lastCapGain": null,
  "lastDividendDate": null,
  "lastDividendValue": null,
  "lastFiscalYearEnd": 1601078400,
  "lastMarket": null,
  "lastSplitDate": null,
  "lastSplitFactor": null,
  "legalType": null,
  "logo_url": "https://logo.clearbit.com/apple.com",
  "longBusinessSummary": "Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. The company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, iPod touch, and other Apple-branded and third-party accessories. It also provides AppleCare support services; cloud services store services; and operates various platforms, including the App Store, that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts. In addition, the company offers various services, such as Apple Arcade, a game subscription service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV+, which offers exclusive original content; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It sells and delivers third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. was founded in 1977 and is headquartered in Cupertino, California.",
  "longName": "Apple Inc.",
  "market": "us_market",
  "marketCap": 2438865616896,
  "maxAge": 1,
  "maxSupply": null,
  "messageBoardId": "finmb_24937",
  "morningStarOverallRating": null,
  "morningStarRiskRating": null,
  "mostRecentQuarter": 1624665600,
  "navPrice": null,
  "netIncomeToCommon": 86801997824,
  "nextFiscalYearEnd": 1664150400,
  "numberOfAnalystOpinions": 41,
  "open": 148.35,
  "openInterest": null,
  "operatingCashflow": 104414003200,
  "operatingMargins": 0.28788,
  "payoutRatio": 0.16309999,
  "pegRatio": 1.34,
  "phone": "408-996-1010",
  "previousClose": 148.36,
  "priceHint": 2,
  "priceToBook": 38.00618,
  "priceToSalesTrailing12Months": 7.025293,
  "profitMargins": 0.25004,
  "quickRatio": 0.887,
  "quoteType": "EQUITY",
  "recommendationKey": "buy",
  "recommendationMean": 2,
  "regularMarketDayHigh": 149.12,
  "regularMarketDayLow": 147.51,
  "regularMarketOpen": 148.35,
  "regularMarketPreviousClose": 148.36,
  "regularMarketPrice": 147.54,
  "regularMarketVolume": 48597195,
  "returnOnAssets": 0.19302,
  "returnOnEquity": 1.27125,
  "revenueGrowth": 0.364,
  "revenuePerShare": 20.61,
  "revenueQuarterlyGrowth": null,
  "sector": "Technology",
  "sharesOutstanding": 16530199552,
  "sharesPercentSharesOut": 0.0056,
  "sharesShort": 93105968,
  "sharesShortPreviousMonthDate": 1626307200,
  "sharesShortPriorMonth": 96355309,
  "shortName": "Apple Inc.",
  "shortPercentOfFloat": 0.0056,
  "shortRatio": 1.19,
  "startDate": null,
  "state": "CA",
  "strikePrice": null,
  "symbol": "AAPL",
  "targetHighPrice": 190,
  "targetLowPrice": 132,
  "targetMeanPrice": 165.87,
  "targetMedianPrice": 168,
  "threeYearAverageReturn": null,
  "toCurrency": null,
  "totalAssets": null,
  "totalCash": 61696000000,
  "totalCashPerShare": 3.732,
  "totalDebt": 135491002368,
  "totalRevenue": 347155005440,
  "tradeable": false,
  "trailingAnnualDividendRate": 0.835,
  "trailingAnnualDividendYield": 0.0056282016,
  "trailingEps": 5.108,
  "trailingPE": 28.884104,
  "twoHundredDayAverage": 133.05403,
  "volume": 48597195,
  "volume24Hr": null,
  "volumeAllCurrencies": null,
  "website": "http://www.apple.com",
  "yield": null,
  "ytdReturn": null,
  "zip": "95014"
}
```

### Analysis

The `/analysis/:symbol` endpoint takes a symbol and return symbol current analysis, such as EPS, Growth, Earnings, Revenue.

Example command:

```bash
curl localhost:8000/analysis/AAPL | jq
```

JSON Response:

```json
{
  "Max Age": {
    "0Q": 1,
    "+1Q": 1,
    "0Y": 1,
    "+1Y": 1,
    "+5Y": 1,
    "-5Y": 1
  },
  "End Date": {
    "0Q": 1640908800000,
    "+1Q": 1648684800000,
    "0Y": 1664496000000,
    "+1Y": 1696032000000,
    "+5Y": null,
    "-5Y": null
  },
  "Growth": {
    "0Q": 0.118999995,
    "+1Q": -0.056999996,
    "0Y": 0.023,
    "+1Y": 0.077,
    "+5Y": 0.1568,
    "-5Y": 0.08415
  },
  "Earnings Estimate Avg": {
    "0Q": 1.88,
    "+1Q": 1.32,
    "0Y": 5.74,
    "+1Y": 6.18,
    "+5Y": null,
    "-5Y": null
  },
  "Earnings Estimate Low": {
    "0Q": 1.75,
    "+1Q": 1.16,
    "0Y": 5.2,
    "+1Y": 5.26,
    "+5Y": null,
    "-5Y": null
  },
  "Earnings Estimate High": {
    "0Q": 1.97,
    "+1Q": 1.52,
    "0Y": 6.27,
    "+1Y": 6.82,
    "+5Y": null,
    "-5Y": null
  },
  "Earnings Estimate Year Ago Eps": {
    "0Q": 1.68,
    "+1Q": 1.4,
    "0Y": 5.61,
    "+1Y": 5.74,
    "+5Y": null,
    "-5Y": null
  },
  "Earnings Estimate Number Of Analysts": {
    "0Q": 25,
    "+1Q": 24,
    "0Y": 37,
    "+1Y": 33,
    "+5Y": null,
    "-5Y": null
  },
  "Earnings Estimate Growth": {
    "0Q": 0.118999995,
    "+1Q": -0.056999996,
    "0Y": 0.023,
    "+1Y": 0.077,
    "+5Y": null,
    "-5Y": null
  },
  "Revenue Estimate Avg": {
    "0Q": 118182000000,
    "+1Q": 90424300000,
    "0Y": 381716000000,
    "+1Y": 401199000000,
    "+5Y": null,
    "-5Y": null
  },
  "Revenue Estimate Low": {
    "0Q": 111806000000,
    "+1Q": 83259000000,
    "0Y": 359156000000,
    "+1Y": 300500000000,
    "+5Y": null,
    "-5Y": null
  },
  "Revenue Estimate High": {
    "0Q": 121303000000,
    "+1Q": 98284000000,
    "0Y": 405435000000,
    "+1Y": 445584000000,
    "+5Y": null,
    "-5Y": null
  },
  "Revenue Estimate Number Of Analysts": {
    "0Q": 22,
    "+1Q": 22,
    "0Y": 36,
    "+1Y": 31,
    "+5Y": null,
    "-5Y": null
  },
  "Revenue Estimate Year Ago Revenue": {
    "0Q": null,
    "+1Q": null,
    "0Y": 365817000000,
    "+1Y": 381716000000,
    "+5Y": null,
    "-5Y": null
  },
  "Revenue Estimate Growth": {
    "0Q": null,
    "+1Q": null,
    "0Y": 0.043,
    "+1Y": 0.051,
    "+5Y": null,
    "-5Y": null
  },
  "Eps Trend Current": {
    "0Q": 1.88,
    "+1Q": 1.32,
    "0Y": 5.74,
    "+1Y": 6.18,
    "+5Y": null,
    "-5Y": null
  },
  "Eps Trend 7Days Ago": {
    "0Q": 1.88,
    "+1Q": 1.32,
    "0Y": 5.74,
    "+1Y": 6.15,
    "+5Y": null,
    "-5Y": null
  },
  "Eps Trend 30Days Ago": {
    "0Q": 1.88,
    "+1Q": 1.32,
    "0Y": 5.75,
    "+1Y": 6.15,
    "+5Y": null,
    "-5Y": null
  },
  "Eps Trend 60Days Ago": {
    "0Q": 1.87,
    "+1Q": 1.29,
    "0Y": 5.68,
    "+1Y": 5.97,
    "+5Y": null,
    "-5Y": null
  },
  "Eps Trend 90Days Ago": {
    "0Q": 1.87,
    "+1Q": 1.28,
    "0Y": 5.72,
    "+1Y": 5.95,
    "+5Y": null,
    "-5Y": null
  },
  "Eps Revisions Up Last7Days": {
    "0Q": 2,
    "+1Q": 1,
    "0Y": 2,
    "+1Y": 2,
    "+5Y": null,
    "-5Y": null
  },
  "Eps Revisions Up Last30Days": {
    "0Q": 3,
    "+1Q": 1,
    "0Y": 4,
    "+1Y": 4,
    "+5Y": null,
    "-5Y": null
  },
  "Eps Revisions Down Last30Days": {
    "0Q": 0,
    "+1Q": 0,
    "0Y": 0,
    "+1Y": 0,
    "+5Y": null,
    "-5Y": null
  },
  "Eps Revisions Down Last90Days": {
    "0Q": null,
    "+1Q": null,
    "0Y": null,
    "+1Y": null,
    "+5Y": null,
    "-5Y": null
  }
}
```

### News

The `/news/:symbol` endpoint takes a symbol and return current news about the company.

Example command:

```bash
curl localhost:8000/news/AAPL | jq
```

JSON Response:

```json
[
  {
    "link": "https://finance.yahoo.com/m/fdb436b3-556d-34e4-8dfe-4d7741d92f12/5-reasons-apple-stock-can.html",
    "providerPublishTime": 1640199300,
    "publisher": "Barrons.com",
    "title": "5 Reasons Apple Stock Can Trade Higher From Here",
    "type": "STORY",
    "uuid": "fdb436b3-556d-34e4-8dfe-4d7741d92f12"
  },
  {
    "link": "https://finance.yahoo.com/news/airline-executives-plead-governments-ease-180000940.html",
    "providerPublishTime": 1640196000,
    "publisher": "Oilprice.com",
    "title": "Airline Executives Plead With Governments To Ease Restrictions",
    "type": "STORY",
    "uuid": "93053731-8504-3351-a42c-75b0533994b4"
  },
  {
    "link": "https://finance.yahoo.com/news/10-value-stocks-buy-according-173231489.html",
    "providerPublishTime": 1640194351,
    "publisher": "Insider Monkey",
    "title": "10 Value Stocks to Buy According to Billionaire Paul Tudor Jones",
    "type": "STORY",
    "uuid": "f41097f9-9fd3-3fc9-be89-d79023773a5d"
  },
  {
    "link": "https://finance.yahoo.com/m/b3389ef7-097c-315b-86f3-fc80a9b0e612/apple-iphone-sales-are.html",
    "providerPublishTime": 1640192340,
    "publisher": "Barrons.com",
    "title": "Apple iPhone Sales Are Stronger Than Expected, Says Morgan Stanley",
    "type": "STORY",
    "uuid": "b3389ef7-097c-315b-86f3-fc80a9b0e612"
  },
  {
    "link": "https://finance.yahoo.com/news/facebook-papers-how-the-2021-leak-could-haunt-meta-in-2022-162233905.html",
    "providerPublishTime": 1640190153,
    "publisher": "Yahoo Finance",
    "title": "Facebook Papers: How the 2021 leak could haunt Meta in 2022",
    "type": "STORY",
    "uuid": "720a7519-b7a7-45b1-bd8b-c5d0855b3988"
  },
  {
    "link": "https://finance.yahoo.com/video/stock-buybacks-set-record-q3-151908752.html",
    "providerPublishTime": 1640186348,
    "publisher": "Yahoo Finance Video",
    "title": "Stock buybacks set record in Q3, led by Apple, Meta, Google",
    "type": "VIDEO",
    "uuid": "f32aef69-9aa3-3670-8969-ea3b1a36f95c"
  },
  {
    "link": "https://finance.yahoo.com/m/65b53896-faf4-3a06-9d0d-a63cf3c83192/5-dow-jones-stocks-to-buy-and.html",
    "providerPublishTime": 1640186133,
    "publisher": "Investor's Business Daily",
    "title": "5 Dow Jones Stocks To Buy And Watch In December 2021: Apple, Microsoft Rise",
    "type": "STORY",
    "uuid": "65b53896-faf4-3a06-9d0d-a63cf3c83192"
  },
  {
    "link": "https://finance.yahoo.com/video/market-check-stocks-open-mixed-150312079.html",
    "providerPublishTime": 1640185392,
    "publisher": "Yahoo Finance Video",
    "title": "Market check: Stocks open mixed, bond volatility settles",
    "type": "VIDEO",
    "uuid": "5075e367-1d24-3713-a0eb-b78167321564"
  }
]
```

### Stats

The `/stats/:symbol` endpoint takes a symbol and return stats about the symbol.

Example command:

```bash
curl localhost:8000/stats/AAPL | jq
```

<details>
<summary>JSON Response:</summary>
<br />

```json
{
  "calendarEvents": {
    "dividendDate": 1636588800,
    "earnings": {
      "earningsAverage": 1.88,
      "earningsDate": [
        1643144400,
        1643662800
      ],
      "earningsHigh": 1.97,
      "earningsLow": 1.75,
      "revenueAverage": 118182000000,
      "revenueHigh": 121303000000,
      "revenueLow": 111806000000
    },
    "exDividendDate": 1636070400,
    "maxAge": 1
  },
  "defaultKeyStatistics": {
    "52WeekChange": 0.32093763,
    "SandP52WeekChange": 0.25995052,
    "annualHoldingsTurnover": null,
    "annualReportExpenseRatio": null,
    "beta": 1.203116,
    "beta3Year": null,
    "bookValue": 3.841,
    "category": null,
    "dateShortInterest": 1638230400,
    "earningsQuarterlyGrowth": 0.622,
    "enterpriseToEbitda": 24.22,
    "enterpriseToRevenue": 7.96,
    "enterpriseValue": 2912025575424,
    "fiveYearAverageReturn": null,
    "floatShares": 16389662475,
    "forwardEps": 6.18,
    "forwardPE": 28.18288,
    "fundFamily": null,
    "fundInceptionDate": null,
    "heldPercentInsiders": 0.00071000005,
    "heldPercentInstitutions": 0.58814996,
    "impliedSharesOutstanding": null,
    "lastCapGain": null,
    "lastDividendDate": 1636070400,
    "lastDividendValue": 0.22,
    "lastFiscalYearEnd": 1632528000,
    "lastSplitDate": 1598832000,
    "lastSplitFactor": "4:1",
    "legalType": null,
    "maxAge": 1,
    "morningStarOverallRating": null,
    "morningStarRiskRating": null,
    "mostRecentQuarter": 1632528000,
    "netIncomeToCommon": 94679998464,
    "nextFiscalYearEnd": 1695600000,
    "pegRatio": 1.92,
    "priceHint": 2,
    "priceToBook": 45.345013,
    "priceToSalesTrailing12Months": null,
    "profitMargins": 0.25882,
    "revenueQuarterlyGrowth": null,
    "sharesOutstanding": 16406400000,
    "sharesPercentSharesOut": 0.0069,
    "sharesShort": 112598907,
    "sharesShortPreviousMonthDate": 1635465600,
    "sharesShortPriorMonth": 100495541,
    "shortPercentOfFloat": 0.0069,
    "shortRatio": 1.4,
    "threeYearAverageReturn": null,
    "totalAssets": null,
    "trailingEps": 5.61,
    "yield": null,
    "ytdReturn": null
  },
  "details": null,
  "earnings": {
    "earningsChart": {
      "currentQuarterEstimate": 1.88,
      "currentQuarterEstimateDate": "4Q",
      "currentQuarterEstimateYear": 2021,
      "earningsDate": [
        1643144400,
        1643662800
      ],
      "quarterly": [
        {
          "actual": 1.68,
          "date": "4Q2020",
          "estimate": 1.41
        },
        {
          "actual": 1.4,
          "date": "1Q2021",
          "estimate": 0.99
        },
        {
          "actual": 1.3,
          "date": "2Q2021",
          "estimate": 1.01
        },
        {
          "actual": 1.24,
          "date": "3Q2021",
          "estimate": 1.24
        }
      ]
    },
    "financialCurrency": "USD",
    "financialsChart": {
      "quarterly": [
        {
          "date": "4Q2020",
          "earnings": 28755000000,
          "revenue": 111439000000
        },
        {
          "date": "1Q2021",
          "earnings": 23630000000,
          "revenue": 89584000000
        },
        {
          "date": "2Q2021",
          "earnings": 21744000000,
          "revenue": 81434000000
        },
        {
          "date": "3Q2021",
          "earnings": 20551000000,
          "revenue": 83360000000
        }
      ],
      "yearly": [
        {
          "date": 2018,
          "earnings": 59531000000,
          "revenue": 265595000000
        },
        {
          "date": 2019,
          "earnings": 55256000000,
          "revenue": 260174000000
        },
        {
          "date": 2020,
          "earnings": 57411000000,
          "revenue": 274515000000
        },
        {
          "date": 2021,
          "earnings": 94680000000,
          "revenue": 365817000000
        }
      ]
    },
    "maxAge": 86400
  },
  "esgScores": {
    "adult": false,
    "alcoholic": false,
    "animalTesting": false,
    "catholic": false,
    "coal": false,
    "controversialWeapons": false,
    "environmentPercentile": null,
    "environmentScore": 0.29,
    "esgPerformance": "UNDER_PERF",
    "furLeather": false,
    "gambling": false,
    "gmo": false,
    "governancePercentile": null,
    "governanceScore": 8.64,
    "highestControversy": 3,
    "maxAge": 86400,
    "militaryContract": false,
    "nuclear": false,
    "palmOil": false,
    "peerCount": 53,
    "peerEnvironmentPerformance": {
      "avg": 3.1907692307692304,
      "max": 8.94,
      "min": 0.03
    },
    "peerEsgScorePerformance": {
      "avg": 16.79754716981132,
      "max": 26.54,
      "min": 7.24
    },
    "peerGovernancePerformance": {
      "avg": 7.425961538461538,
      "max": 13.89,
      "min": 3.45
    },
    "peerGroup": "Technology Hardware",
    "peerHighestControversyPerformance": {
      "avg": 1.5660377358490567,
      "max": 4,
      "min": 0
    },
    "peerSocialPerformance": {
      "avg": 6.3628846153846155,
      "max": 12.55,
      "min": 2.24
    },
    "percentile": 13.68,
    "pesticides": false,
    "ratingMonth": 9,
    "ratingYear": 2021,
    "relatedControversy": [
      "Social Supply Chain Incidents",
      "Customer Incidents",
      "Business Ethics Incidents"
    ],
    "smallArms": false,
    "socialPercentile": null,
    "socialScore": 7.99,
    "tobacco": false,
    "totalEsg": 16.92
  },
  "financialData": {
    "currentPrice": 174.1702,
    "currentRatio": 1.075,
    "debtToEquity": 216.392,
    "earningsGrowth": 0.662,
    "ebitda": 120233000960,
    "ebitdaMargins": 0.32867,
    "financialCurrency": "USD",
    "freeCashflow": 73295003648,
    "grossMargins": 0.41779,
    "grossProfits": 152836000000,
    "maxAge": 86400,
    "numberOfAnalystOpinions": 42,
    "operatingCashflow": 104037998592,
    "operatingMargins": 0.29782,
    "profitMargins": 0.25882,
    "quickRatio": 0.91,
    "recommendationKey": "buy",
    "recommendationMean": 1.8,
    "returnOnAssets": 0.20179,
    "returnOnEquity": 1.47443,
    "revenueGrowth": 0.288,
    "revenuePerShare": 21.904,
    "targetHighPrice": 210,
    "targetLowPrice": 128.01,
    "targetMeanPrice": 174.22,
    "targetMedianPrice": 172,
    "totalCash": 62639001600,
    "totalCashPerShare": 3.818,
    "totalDebt": 136521998336,
    "totalRevenue": 365817004032
  },
  "financialsTemplate": {
    "code": "N",
    "maxAge": 1
  },
  "pageViews": {
    "longTermTrend": "UP",
    "maxAge": 1,
    "midTermTrend": "UP",
    "shortTermTrend": "DOWN"
  },
  "price": {
    "averageDailyVolume10Day": 130379400,
    "averageDailyVolume3Month": 89826615,
    "circulatingSupply": null,
    "currency": "USD",
    "currencySymbol": "$",
    "exchange": "NMS",
    "exchangeDataDelayedBy": 0,
    "exchangeName": "NasdaqGS",
    "fromCurrency": null,
    "lastMarket": null,
    "longName": "Apple Inc.",
    "marketCap": 2857505914880,
    "marketState": "REGULAR",
    "maxAge": 1,
    "openInterest": null,
    "postMarketChange": null,
    "postMarketPrice": null,
    "preMarketChange": 0.00959778,
    "preMarketChangePercent": 5.5481698e-05,
    "preMarketPrice": 173,
    "preMarketSource": "FREE_REALTIME",
    "preMarketTime": 1640183396,
    "priceHint": 2,
    "quoteSourceName": "Nasdaq Real Time Price",
    "quoteType": "EQUITY",
    "regularMarketChange": 1.180191,
    "regularMarketChangePercent": 0.0068223076,
    "regularMarketDayHigh": 174.75,
    "regularMarketDayLow": 172.16,
    "regularMarketOpen": 173.04,
    "regularMarketPreviousClose": 172.99,
    "regularMarketPrice": 174.1702,
    "regularMarketSource": "FREE_REALTIME",
    "regularMarketTime": 1640202160,
    "regularMarketVolume": 59520625,
    "shortName": "Apple Inc.",
    "strikePrice": null,
    "symbol": "AAPL",
    "toCurrency": null,
    "underlyingSymbol": null,
    "volume24Hr": null,
    "volumeAllCurrencies": null
  },
  "quoteType": {
    "exchange": "NMS",
    "exchangeTimezoneName": "America/New_York",
    "exchangeTimezoneShortName": "EST",
    "gmtOffSetMilliseconds": "-18000000",
    "isEsgPopulated": false,
    "longName": "Apple Inc.",
    "market": "us_market",
    "messageBoardId": "finmb_24937",
    "quoteType": "EQUITY",
    "shortName": "Apple Inc.",
    "symbol": "AAPL"
  },
  "recommendationTrend": {
    "maxAge": 86400,
    "trend": [
      {
        "buy": 21,
        "hold": 6,
        "period": "0m",
        "sell": 0,
        "strongBuy": 11,
        "strongSell": 0
      },
      {
        "buy": 21,
        "hold": 7,
        "period": "-1m",
        "sell": 0,
        "strongBuy": 13,
        "strongSell": 0
      },
      {
        "buy": 20,
        "hold": 8,
        "period": "-2m",
        "sell": 0,
        "strongBuy": 13,
        "strongSell": 0
      },
      {
        "buy": 20,
        "hold": 8,
        "period": "-3m",
        "sell": 0,
        "strongBuy": 13,
        "strongSell": 0
      }
    ]
  },
  "summaryDetail": {
    "algorithm": null,
    "ask": 173.95,
    "askSize": 800,
    "averageDailyVolume10Day": 130379400,
    "averageVolume": 89826615,
    "averageVolume10days": 130379400,
    "beta": 1.203116,
    "bid": 173.9,
    "bidSize": 800,
    "circulatingSupply": null,
    "currency": "USD",
    "dayHigh": 174.75,
    "dayLow": 172.16,
    "dividendRate": 0.88,
    "dividendYield": 0.0050999997,
    "exDividendDate": 1636070400,
    "expireDate": null,
    "fiftyDayAverage": 157.4756,
    "fiftyTwoWeekHigh": 182.13,
    "fiftyTwoWeekLow": 116.21,
    "fiveYearAvgDividendYield": 1.2,
    "forwardPE": 28.18288,
    "fromCurrency": null,
    "lastMarket": null,
    "marketCap": 2857505914880,
    "maxAge": 1,
    "maxSupply": null,
    "navPrice": null,
    "open": 173.04,
    "openInterest": null,
    "payoutRatio": 0.1515,
    "previousClose": 172.99,
    "priceHint": 2,
    "priceToSalesTrailing12Months": 7.811299,
    "regularMarketDayHigh": 174.75,
    "regularMarketDayLow": 172.16,
    "regularMarketOpen": 173.04,
    "regularMarketPreviousClose": 172.99,
    "regularMarketVolume": 59520625,
    "startDate": null,
    "strikePrice": null,
    "toCurrency": null,
    "totalAssets": null,
    "tradeable": false,
    "trailingAnnualDividendRate": 0.85,
    "trailingAnnualDividendYield": 0.0049135787,
    "trailingPE": 31.046381,
    "twoHundredDayAverage": 142.0093,
    "volume": 59520625,
    "volume24Hr": null,
    "volumeAllCurrencies": null,
    "yield": null,
    "ytdReturn": null
  },
  "summaryProfile": {
    "address1": "One Apple Park Way",
    "city": "Cupertino",
    "companyOfficers": [],
    "country": "United States",
    "fullTimeEmployees": 154000,
    "industry": "Consumer Electronics",
    "longBusinessSummary": "Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. In addition, the company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; AirPods Max, an over-ear wireless headphone; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, and iPod touch. Further, it provides AppleCare support services; cloud services store services; and operates various platforms, including the App Store that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts. Additionally, the company offers various services, such as Apple Arcade, a game subscription service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV+, which offers exclusive original content; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It distributes third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. was incorporated in 1977 and is headquartered in Cupertino, California.",
    "maxAge": 86400,
    "phone": "408 996 1010",
    "sector": "Technology",
    "state": "CA",
    "website": "https://www.apple.com",
    "zip": "95014"
  },
  "symbol": "AAPL",
  "upgradeDowngradeHistory": {
    "history": [
      {
        "action": "main",
        "epochGradeDate": 1640184748,
        "firm": "Citigroup",
        "fromGrade": "",
        "toGrade": "Buy"
      }
      ...
    ],
    "maxAge": 86400
  }
}
```

</details>

## Credits

This software uses the following open source packages:

- [yfinance](https://pypi.org/project/yfinance/)
- [gunicorn](https://gunicorn.org/)
- [Flask](https://flask.palletsprojects.com)

## License

PY-Stocks is released under the [MIT License](https://opensource.org/licenses/MIT).

