# api_data.py
import requests
import json

def get_news(ticker_list,start,end):
    symbols=ticker_list
    limit=5
    #start="2024-07-01"
    #end="2024-07-30"
    url = f"https://data.alpaca.markets/v1beta1/news?start={start}T00%3A00%3A00Z&end={end}T00%3A00%3A00Z&sort=desc&symbols={"%2C".join(symbols)}&limit={limit}&include_content=true&exclude_contentless=true"

    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": "PKQWXGFE14OPQE8M0VIN",
        "APCA-API-SECRET-KEY": "d6CjPOCYpjg1as2nab6PP1iCYmOvqv6FvrzVKJS4"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        articles = []
        for article in data["news"]:
            articles.append({
                "headline": article["headline"],
                "url": article["url"],
                "date":article["created_at"]
            })
        return articles
    else:
        return None  # Handle failure case

    # "APCA-API-KEY-ID": "PKQWXGFE14OPQE8M0VIN",
    # "APCA-API-SECRET-KEY": "d6CjPOCYpjg1as2nab6PP1iCYmOvqv6FvrzVKJS4"
    {
  "news": [
    {
      "author": "Chris Katje",
      "content": "<p>Electric vehicle leader <strong>Tesla Inc</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/TSLA#NASDAQ\">TSLA</a>) launched several video game initiatives over the years, which shouldn't be a surprise given CEO <strong>Elon Musk's</strong> <a href=\"https://www.benzinga.com/markets/cryptocurrency/22/06/27881697/happy-birthday-elon-musk-52-facts-and-figures-about-tesla-and-spacex-ceo-on-his-52nd-birth\">love of video games.</a></p>\n\n\n\n<p>Tesla owners could have a new competitive video game feature.</p>\n\n\n\n<p><strong>What Happened:</strong> Tesla is one of the leaders in <a href=\"https://www.benzinga.com/news/24/05/38541246/tesla-ceo-elon-musk-says-supercharger-network-will-still-grow-but-at-a-slower-pace-for-new-locations\">electric vehicle charging infrastructure</a>. The company's Supercharger locations are available for Tesla owners and in recent years have expanded to open up to other auto companies.</p>\n\n\n\n<p>Owners of Tesla vehicles could soon have a new reason to head to their local Supercharger station instead of charging their vehicles at home.</p>\n\n\n\n<p>Playable game <strong>\"Beach Buggy Racing\" </strong>could soon have local leaderboards at Supercharger stations, <a href=\"https://www.teslarati.com/tesla-adding-supercharger-racing-game-leaderboards-with-next-update/amp/\">reported </a>Teslarati.</p>\n\n\n\n<p>The report, which cited release <a href=\"https://www.notateslaapp.com/software-updates/version/2024.20/release-notes\">notes </a>from Not a Tesla App, said Tesla users will be able to compete in special races of the game and compete for leaderboard spots at Supercharger locations.</p>\n\n\n\n<p>\"Set the fastest lap at your local Supercharger! Drive to a Supercharger and compete in Beach Buddy Racing special races to set the fastest time on the leaderboard against other players,\" Tesla's release notes said, according to the report.</p>\n\n\n\n<p>The leaderboard is expected to roll out in the U.S. in the latest update. Other updates center on security and hot weather improvements.</p>\n\n\n\n<p><em>Related Link: <a href=\"https://www.benzinga.com/news/earnings/24/04/38390883/tesla-q1-earnings-highlights-ev-giant-misses-wall-street-estimates-makes-cost-cuts-invests-in-ai-sp\">Tesla Q1 Earnings Highlights: EV Giant Misses Wall Street Estimates, Makes Cost Cuts, Invests In AI, Speeds Launch Of New Models</a></em></p>\n\n\n\n<p><strong>Why It's Important:</strong> Having <a href=\"https://www.benzinga.com/general/gaming/22/07/28103366/tesla-video-game-features-about-to-get-a-huge-upgrade-heres-the-details\">playable video games </a>in Tesla vehicles and streaming platforms are among the features that could make a trip to a charging location go by faster than simply sitting in a parked vehicle.</p>\n\n\n\n<p>Tesla charging locations in Germany <a href=\"https://www.benzinga.com/news/22/08/28359622/dip-in-the-pool-while-your-ev-charges-heres-how-tesla-could-be-changing-the-waiting-game\">feature swimming pools.</a></p>\n\n\n\n<p>In California, a Tesla Supercharger station is working on <a href=\"https://www.benzinga.com/news/24/03/37465922/teslas-la-supercharger-installs-first-movie-screen-for-drive-in-will-doge-payments-be-accepted\">having a drive-in movie theater </a>and diner, which could also make the wait time to charge a vehicle go by in the blink of an eye.</p>\n\n\n\n<p>The new video game feature is another way Tesla is increasing the functionality of features inside electric vehicles.</p>\n\n\n\n<p><em>Read Next: <a href=\"https://www.benzinga.com/general/gaming/24/02/37196810/elon-musk-opens-up-on-when-tesla-will-make-a-video-game-ive-wanted-to-do-that-for-a-long-time\">Elon Musk Opens Up On When Tesla Will Make A Video Game: &#8216;I&#8217;ve Wanted To Do That For A Long Time&#8217;</a></em></p>\n\n\n\n<p><em>Photo: Sheila Fitzgerald on Shutterstock</em></p>\n\n\n\n<p><em>Check Out: The average American couple has saved this much money for retirement — <a href=\"http://www.benzinga.com/money/smartasset\" target=\"_blank\" rel=\"noreferrer noopener\">How do you compare</a>?</em></p>",
      "created_at": "2024-05-29T23:02:43Z",
      "headline": "Tesla Owners Could Soon Play Video Games At Supercharger Stations",
      "id": 39076303,
      "images": [
        {
          "size": "large",
          "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2024/05/29/Kettleman-City--Ca---Jan-29--2022-Many-C.jpeg"
        },
        {
          "size": "small",
          "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2024/05/29/Kettleman-City--Ca---Jan-29--2022-Many-C.jpeg"
        },
        {
          "size": "thumb",
          "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2024/05/29/Kettleman-City--Ca---Jan-29--2022-Many-C.jpeg"
        }
      ],
      "source": "benzinga",
      "summary": "Tesla owners can play many video games inside their vehicles. One game could be part of a localized leaderboard feature for Supercharger locations.",
      "symbols": [
        "TSLA"
      ],
      "updated_at": "2024-05-29T23:02:44Z",
      "url": "https://www.benzinga.com/general/gaming/24/05/39076303/tesla-owners-could-soon-play-video-games-at-supercharger-stations"
    },
    {
      "author": "Piero Cingari",
      "content": "<p><strong>NVIDIA Corp. </strong>(NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/NVDA#NASDAQ\">NVDA</a>) has been the standout tech stock of the past year, leading the<strong> Nasdaq 100 index</strong> <a href=\"https://www.benzinga.com/quote/NVDA/news\">in the performance ranking.</a></p>\n\n\n\n<p>The chipmaker giant has seen an astounding 186% surge since the end of May 2023, fueled by skyrocketing demand for chips in artificial intelligence development.</p>\n\n\n\n<p>Veteran Wall Street investor <strong>Ed Yardeni </strong>recently coined &#8220;Magnificent One&#8221; to differentiate Nvidia&#8217;s extraordinary performance <a href=\"https://www.benzinga.com/analyst-ratings/analyst-color/24/05/39037833/magnificent-7-becomes-the-magnificent-one-wall-street-guru-hails-single-tech-stock-\">from the Magnificent Seven.</a></p>\n\n\n\n<p>To illustrate the magnitude of Nvidia's market value increase, just a year ago, the company was valued at $1 trillion. Today, it boasts a staggering $2.8 trillion valuation, making it the third-largest company in the U.S. </p>\n\n\n\n<p>Nvidia&#8217;s current value is equal to <strong>Tesla Inc.</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/TSLA#NASDAQ\">TSLA</a>), <strong>Ely Lilly &amp; Co</strong>. (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/LLY#NYSE\">LLY</a>), <strong>Broadcom Inc.</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/AVGO#NASDAQ\">AVGO</a>), <strong>Walmart Inc.</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/WMT#NYSE\">WMT</a>) and <strong>Mastercard Inc.</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/MA#NYSE\">MA</a>) combined.</p>\n\n\n\n<p><em>Read Also: <a href=\"https://www.benzinga.com/general/education/24/05/39063462/when-will-nvidia-be-the-most-valuable-company-in-the-world\">When Will Nvidia Be The Most Valuable Company In The World?</a></em></p>\n\n\n\n<p>However, Nvidia's spectacular ascent is eclipsed by these seven U.S. stocks, which have more than doubled the chipmaker&#8217;s impressive returns over the last year.</p>\n\n\n\n<h1 class=\"wp-block-heading\"><strong>7. Vera Therapeutics, Inc. </strong>(NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/VERA#NASDAQ\">VERA</a>):<strong> 363%</strong></h1>\n\n\n\n<p>Vera Therapeutics is a biopharmaceutical company dedicated to developing transformative treatments for serious immunological diseases. The company&#8217;s stock surged due to advancements in its clinical programs and optimistic projections for its drug candidates. </p>\n\n\n\n<p>Its 363% surge since May 30, 2023, doubled the performance of Nvidia during the same timeframe.</p>\n\n\n\n<h1 class=\"wp-block-heading\"><strong>6. Vertiv Holdings Co. </strong>(NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/VRT#NYSE\">VRT</a>):<strong> 413%</strong></h1>\n\n\n\n<p>Vertiv Holdings Co. provides critical digital infrastructure and continuity solutions. The company has benefited from the increasing demand for data centers and IT infrastructure, driving robust financial performance and, consequently, a substantial increase in its stock price.</p>\n\n\n\n<h1 class=\"wp-block-heading\"><strong>5. MicroStrategy Incorporated </strong>(NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/MSTR#NASDAQ\">MSTR</a>)<strong>: 441%</strong></h1>\n\n\n\n<p>MicroStrategy Incorporated is a business intelligence company that has gained substantial attention for its significant investments in <strong>Bitcoin</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/btc/usd\">BTC</a>). </p>\n\n\n\n<p>The company&#8217;s stock performance is closely tied to Bitcoin&#8217;s price movements, and its value has soared with the cryptocurrency&#8217;s rise. The largest cryptocurrency has seen a 140% rise since the end of May 2023.</p>\n\n\n\n<h1 class=\"wp-block-heading\"><strong>4. Abercrombie &amp; Fitch Co. </strong>(NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/ANF#NYSE\">ANF</a>):<strong> 503%</strong></h1>\n\n\n\n<p>Abercrombie &amp; Fitch is a renowned fashion retailer, known for its casual wear and lifestyle products. The stock&#8217;s impressive rise is attributed to the company's successful rebranding efforts, strong e-commerce growth and improved profitability metrics, attracting investor interest.</p>\n\n\n\n<h1 class=\"wp-block-heading\"><strong>3. Carvana Co. </strong>(NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/CVNA#NASDAQ\">CVNA</a>):<strong> 666%</strong></h1>\n\n\n\n<p>Carvana is an online used car retailer that has revolutionized the car buying experience by offering a fully online platform with home delivery and a seven-day return policy. </p>\n\n\n\n<p>Its stock skyrocketed as the company continued to recover from a difficult period and investors regained confidence in its unique business model and growth potential.</p>\n\n\n\n<h1 class=\"wp-block-heading\"><strong>2. Soleno Therapeutics, Inc. </strong>(NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/SLNO#NASDAQ\">SLNO</a>):<strong> 697%</strong></h1>\n\n\n\n<p>Soleno Therapeutics focuses on developing treatments for rare diseases, with a primary emphasis on genetic disorders such as Prader-Willi syndrome. The company&#8217;s stock has surged due to positive clinical trial results and increased optimism about its pipeline of drug candidates.</p>\n\n\n\n<h1 class=\"wp-block-heading\"><strong>1. MoneyLion Inc. </strong>(NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/ML#NYSE\">ML</a>)<strong>: 790%</strong></h1>\n\n\n\n<p>MoneyLion Inc. is a digital financial platform offering a range of products, including personal loans, credit-building services, and financial advisory tools. Its significant stock surge is driven by aggressive expansion and innovation in fintech services, appealing to a broad customer base looking for accessible financial solutions.</p>\n\n\n\n<figure class=\"wp-block-image size-large\"><img loading=\"lazy\" decoding=\"async\" width=\"1024\" height=\"500\" src=\"https://editorial-assets.benzinga.com/wp-content/uploads/2024/05/29161150/image-119-1024x500.png\" alt=\"\" class=\"wp-image-361859\" srcset=\"https://editorial-assets.benzinga.com/wp-content/uploads/2024/05/29161150/image-119-1024x500.png 1024w,https://editorial-assets.benzinga.com/wp-content/uploads/2024/05/29161150/image-119-300x147.png 300w,https://editorial-assets.benzinga.com/wp-content/uploads/2024/05/29161150/image-119-768x375.png 768w,https://editorial-assets.benzinga.com/wp-content/uploads/2024/05/29161150/image-119-1536x750.png 1536w,https://editorial-assets.benzinga.com/wp-content/uploads/2024/05/29161150/image-119.png 1920w\" sizes=\"(max-width: 1024px) 100vw, 1024px\" /></figure>\n\n\n\n<p><em>Photo: Shutterstock</em><br></p>\n\n\n\n<p><em><strong>Don&#8217;t Miss:</strong> The average American couple has saved this much money for retirement — <a href=\"http://www.benzinga.com/money/smartasset\" target=\"_blank\" rel=\"noreferrer noopener\">How do you compare</a>?</em></p>    ",
      "created_at": "2024-05-29T21:56:11Z",
      "headline": "Nvidia Is Up 186% From A Year Ago, Yet These 7 Stocks Have More Than Doubled Their Returns Over The AI Chipmaker",
      "id": 39075857,
      "images": [
        {
          "size": "large",
          "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2024/05/29/StockMarket-Up-Shutterstock.jpeg"
        },
        {
          "size": "small",
          "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2024/05/29/StockMarket-Up-Shutterstock.jpeg"
        },
        {
          "size": "thumb",
          "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2024/05/29/StockMarket-Up-Shutterstock.jpeg"
        }
      ],
      "source": "benzinga",
      "summary": "NVIDIA Corp. (NASDAQ:NVDA) has been the standout tech stock of the past year, leading the Nasdaq 100 index in the performance ranking.",
      "symbols": [
        "ANF",
        "AVGO",
        "BTCUSD",
        "CVNA",
        "LLY",
        "MA",
        "ML",
        "MSTR",
        "NVDA",
        "SLNO",
        "TSLA",
        "VERA",
        "VRT",
        "WMT"
      ],
      "updated_at": "2024-05-29T21:56:12Z",
      "url": "https://www.benzinga.com/general/biotech/24/05/39075857/nvidia-is-up-186-from-a-year-ago-yet-these-7-stocks-have-more-than-doubled-their-returns-over-the"
    },
    {
      "author": "Ivan Crnogatić",
      "content": "<p>Cryptocurrency markets traded within a tight downward range on Wednesday, as traditional markets had a rocky trading day <a href=\"https://www.benzinga.com/24/05/39066480/vix-rises-8-treasury-yields-jump-dow-plunges-why-is-wall-street-wobbling-thursday\">with increased volatility</a>.</p>\n\n\n\n<p><strong>Prices as of 4:00 p.m. ET:</strong></p>\n\n\n\n<figure class=\"wp-block-table\"><table><tbody><tr><td><strong>Cryptocurrency</strong></td><td><strong>Price</strong></td><td><strong>Gains +/-</strong></td></tr><tr><td><strong>Bitcoin</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/btc/usd\">BTC</a>)</td><td>$67,140</td><td>-1.9%</td></tr><tr><td><strong>Ethereum</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/eth/usd\">ETH</a>)</td><td>$3,745</td><td>-2.6%</td></tr><tr><td><strong>Solana</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/sol/usd\">SOL</a>)</td><td>$169.00</td><td>-0.7%</td></tr><tr><td><strong>Dogecoin </strong>(CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/doge/usd\">DOGE</a>)</td><td>$0.165</td><td>+0.2%</td></tr><tr><td><strong>Shiba Inu</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/shib/usd\">SHIB</a>)</td><td>$0.0000275</td><td>+3.8%</td></tr></tbody></table></figure>\n\n\n\n<p><strong>Notable Statistics:</strong></p>\n\n\n\n<ul>\n<li><a href=\"https://www.coinglass.com/LiquidationData\">Liquidations</a> declined from $170 million on Tuesday to just over $100 million on Wednesday at the time of writing, with over $75 million in longs liquidated.</li>\n\n\n\n<li><a href=\"https://www.coinglass.com/options\">Options data</a> shows 65% of outstanding positions in call options, betting on increasing prices.</li>\n\n\n\n<li>The long/short ratio was split almost 50/50, with 50.80% of traders taking short positions at the time of writing.</li>\n</ul>\n\n\n\n<p><strong>Notable Developments:</strong></p>\n\n\n\n<ul>\n<li><a href=\"https://www.benzinga.com/markets/cryptocurrency/24/05/39072128/exclusive-can-brett-become-the-shiba-inu-of-the-base-blockchain\">EXCLUSIVE: Can BRETT Become The Shiba Inu Of The Base Blockchain?</a></li>\n\n\n\n<li><a href=\"https://www.benzinga.com/markets/cryptocurrency/24/05/39067327/trump-guilty-verdict-in-hush-money-trial-76-chance-say-crypto-bettors-on-prediction-market\">Trump Guilty Verdict In Hush Money Trial? 76% Chance, Say Crypto Bettors On Prediction Market</a></li>\n\n\n\n<li><a href=\"https://www.benzinga.com/markets/cryptocurrency/24/05/39070528/dogecoin-is-the-easiest-play-will-2x-instantly-once-it-starts-moving-bullish-traders-predi\">Dogecoin Is &#8216;The Easiest Play, &#8216;Will 2x Instantly&#8217; Once It Starts Moving, Bullish Traders Predict</a></li>\n\n\n\n<li><a href=\"https://www.benzinga.com/markets/cryptocurrency/24/05/39068774/paypal-launches-pyusd-stablecoin-on-solana\">PayPal Launches PYUSD Stablecoin On Solana</a></li>\n\n\n\n<li><a href=\"https://www.benzinga.com/markets/cryptocurrency/24/05/39049713/exclusive-will-ethereum-etfs-lead-to-new-all-time-highs-50-of-holders-say-they-would-sell-\">EXCLUSIVE: Will Ethereum ETFs Lead To New All-Time Highs? 50% Of Holders Say They Would Sell At This Price</a></li>\n</ul>\n\n\n\n<figure class=\"wp-block-image size-full\"><a href=\"https://www.benzinga.com/events/digital-assets/\"><img loading=\"lazy\" decoding=\"async\" width=\"300\" height=\"250\" src=\"https://editorial-assets.benzinga.com/wp-content/uploads/2024/03/27091545/Benzinga-conference.gif\" alt=\"Benzinga future of digital assets conference\" class=\"wp-image-267246\"/></a></figure>\n\n\n\n<p></p>\n\n\n\n<h3 class=\"wp-block-heading\"><strong>Top Gainers:</strong></h3>\n\n\n\n<figure class=\"wp-block-table\"><table><tbody><tr><td><strong>Cryptocurrency</strong></td><td><strong>Price</strong></td><td><strong>Gains +/</strong>–</td></tr><tr><td><strong>Worldcoin</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/\">WLD</a>)</td><td>$4.84</td><td>+4%</td></tr><tr><td><strong>Dogwifhat</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/\">WIF</a>)</td><td>$3.82</td><td>+4%</td></tr><tr><td><strong>Bitget Token</strong> (CRYPTO: BGB)</td><td>$1.32</td><td>+3.8%</td></tr></tbody></table></figure>\n\n\n\n<p><strong>Trader Notes:</strong> Trader notes were unusually muted due to low volatility.<strong> </strong></p>\n\n\n\n<p><strong>BecauseBitcoin</strong> CEO Max pointed out the historical price movement of Bitcoin in election and post-election years. </p>\n\n\n\n<p>Prices rallied for one year after each election, he noted.</p>\n\n\n\n<figure class=\"wp-block-embed is-type-rich is-provider-twitter wp-block-embed-twitter\"><div class=\"wp-block-embed__wrapper\">\n<blockquote class=\"twitter-tweet\" data-width=\"500\" data-dnt=\"true\"><p lang=\"en\" dir=\"ltr\">Here is <a href=\"https://twitter.com/hashtag/Bitcoin?src=hash&amp;ref_src=twsrc%5Etfw\">#Bitcoin</a> overlayed with the most recent US Presidential Elections. <br><br>Very interesting to see how price navigates leading into the election &amp; then afterward. <br><br>Notice the grey boxes at each cycle top &#8211; Historically, price has rallied for roughly 1 year after each election <a href=\"https://t.co/Y8fFtw9j7B\">pic.twitter.com/Y8fFtw9j7B</a></p>&mdash; Max (@MaxBecauseBTC) <a href=\"https://twitter.com/MaxBecauseBTC/status/1795853733877752199?ref_src=twsrc%5Etfw\">May 29, 2024</a></blockquote><script async src=\"https://platform.twitter.com/widgets.js\" charset=\"utf-8\"></script>\n</div></figure>\n\n\n\n<p>Bitcoin-based firm <strong>Unchained</strong> highlighted that over half of all bitcoin have not been moved since May 2022, despite several bearish catalysts occurring in the meantime. This underscores a much-talked about point by Bitcoin advocates—the currency&#8217;s famously inelastic supply.</p>\n\n\n\n<figure class=\"wp-block-embed is-type-rich is-provider-twitter wp-block-embed-twitter\"><div class=\"wp-block-embed__wrapper\">\n<blockquote class=\"twitter-tweet\" data-width=\"500\" data-dnt=\"true\"><p lang=\"en\" dir=\"ltr\">~55% of all <a href=\"https://twitter.com/hashtag/bitcoin?src=hash&amp;ref_src=twsrc%5Etfw\">#bitcoin</a> have remained unmoved since May 2022, despite:<br><br>&#8211; Implosion of nearly all bitcoin yield products<br>&#8211; Collapse of Terra Luna<br>&#8211; FTX bankruptcy<br>&#8211; Approval and launch of spot bitcoin ETFs<br>&#8211; Savers upgrading to multisig<br>&#8211; Consolidation of UTXOs <a href=\"https://t.co/Gqz9nKJq8e\">pic.twitter.com/Gqz9nKJq8e</a></p>&mdash; Unchained (@unchainedcom) <a href=\"https://twitter.com/unchainedcom/status/1795838908154196471?ref_src=twsrc%5Etfw\">May 29, 2024</a></blockquote><script async src=\"https://platform.twitter.com/widgets.js\" charset=\"utf-8\"></script>\n</div></figure>\n\n\n\n<p><strong>What&#8217;s Next:</strong>&nbsp;The influence of&nbsp;<a href=\"https://www.benzinga.com/money/is-bitcoin-a-good-investment\" target=\"_blank\" rel=\"noreferrer noopener\">Bitcoin as an institutional asset class</a>&nbsp;is expected to be thoroughly explored at Benzinga&#8217;s upcoming&nbsp;<a href=\"https://www.benzinga.com/events/digital-assets/agenda/\" target=\"_blank\" rel=\"noreferrer noopener\">Future of Digital Assets</a>&nbsp;event on Nov. 19.</p>\n\n\n\n<p><em>Read Next:&nbsp;<a href=\"https://www.benzinga.com/markets/cryptocurrency/24/05/39032058/shiba-inu-investor-turns-2-625-investment-in-dogecoin-killer-to-1-1m-afer-3-5-years-of-ina\">Shiba Inu Investor Turns $2,625 Investment In &#8216;Dogecoin Killer&#8217; To $1.1M Afer 3.5 Years Of Inactivity</a></em></p>\n\n\n\n<p><em>Photo: Shutterstock</em></p>    ",
      "created_at": "2024-05-29T20:36:27Z",
      "headline": "Bitcoin, Ethereum, Dogecoin Grind Lower; Shiba Inu Outperforms: 'Price Rallied For 1 Year After Election,' Trader Says",
      "id": 39074235,
      "images": [
        {
          "size": "large",
          "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2024/05/29/Background-Form-Crypto-Currency-Coins.jpeg"
        },
        {
          "size": "small",
          "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2024/05/29/Background-Form-Crypto-Currency-Coins.jpeg"
        },
        {
          "size": "thumb",
          "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2024/05/29/Background-Form-Crypto-Currency-Coins.jpeg"
        }
      ],
      "source": "benzinga",
      "summary": "Cryptocurrency markets traded within a tight downward range on Wednesday, as traditional markets had a rocky trading day with increased volatility.\n\n\n\nPrices as of 4:00 p.m. ET:",
      "symbols": [
        "BTCUSD",
        "DOGEUSD",
        "ETHUSD",
        "SHIBUSD",
        "SOLUSD"
      ],
      "updated_at": "2024-05-29T20:36:28Z",
      "url": "https://www.benzinga.com/markets/cryptocurrency/24/05/39074235/bitcoin-ethereum-dogecoin-grind-lower-shiba-inu-outperforms-price-rallied-for-1-year-after"
    },
    {
      "author": "Murtuza Merchant",
      "content": "<p><strong>BRETT </strong>(CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/\">BRETT</a>), <a href=\"https://www.benzinga.com/analyst-ratings/analyst-color/24/04/38105117/meme-coin-on-coinbases-layer-2-network-could-rise-80-towards-new-all-time-high-says\">a meme coin</a> inspired by the character of the same name from the popular comic series &#8220;Boys Club,&#8221; is aiming to become the dominant meme coin on the <strong>Base</strong> blockchain, according to <strong>Crash</strong>, a representative of the BRETT community.</p>\n\n\n\n<p>Much like how <strong>Shiba Inu</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/shib/usd\">SHIB</a>) rose on <strong>Ethereum </strong>(CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/eth/usd\">ETH</a>) and <strong>WIF </strong>(CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/\">WIF</a>) on <strong>Solana </strong>(CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/sol/usd\">SOL</a>), BRETT is positioning itself as the leading meme coin on the Base chain, Crash said, in an interview with Benzinga.</p>\n\n\n\n<p>Crash, <a href=\"https://www.benzinga.com/markets/cryptocurrency/24/04/38109345/trader-turns-15k-into-5-5m-with-brett-refuses-to-sell-this-is-the-shib-of-this-bull-run\">a prominent advocate for BRETT</a>, shared insights into the coin&#8217;s origins and future during a recent interview.</p>\n\n\n\n<p>&#8220;BRETT is a main character from the comic series &#8216;Boys Club&#8217; made by Matt Furie. The first two characters Matt drew were Pepe and Brett,&#8221; Crash explained, emphasizing the cultural roots of the coin. </p>\n\n\n\n<p>This connection to the well-known <strong>Pepe </strong>(CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/\">PEPE</a>) meme adds a layer of authenticity and appeal to the coin.</p>\n\n\n\n<p>When asked about the development team behind BRETT, Crash highlighted the decentralized nature of meme coins. </p>\n\n\n\n<p>&#8220;I help where I can. I see other community members constantly posting and spreading the word. These are decentralized meme coins; anybody and everybody in the world is working on spreading BRETT,&#8221; he said. </p>\n\n\n\n<p>This collective effort by the community enhances the network&#8217;s value and the token itself.</p>\n\n\n\n<p>Discussing the potential of BRETT, Crash expressed high expectations for its market performance. </p>\n\n\n\n<p>&#8220;BRETT is gonna go to $1.00-$3.00+ easily this cycle. It&#8217;s at 7 cents right now. The market will decide the value, and I believe I know what the market will value BRETT at as the #1 memecoin on Base,&#8221; he said. </p>\n\n\n\n<p>Crash drew parallels to previous successes, noting that as the top meme coin on the Base chain, BRETT could achieve a market cap of over $10 billion, similar to how WIF and SHIB performed relative to their respective chains.</p>\n\n\n\n<p>Crash also touched on the broader trend of meme coins in the cryptocurrency market. &#8220;Meme coins are the new altcoins, the new bubble trade of this cycle,&#8221; he explained. </p>\n\n\n\n<p><em>Also Read: <a href=\"https://www.benzinga.com/markets/cryptocurrency/24/05/39062709/cathie-wood-el-salvadors-bitcoin-and-ai-push-could-grow-its-gdp-10x-in-5-years\">Cathie Wood: El Salvador&#8217;s Bitcoin And AI Push Could Grow Its GDP 10X In 5 Years</a></em></p>\n\n\n\n<p>Reflecting on past market cycles, he predicted that the 2024-2025 period would see meme coins reaching unprecedented valuations, much like SHIB and <strong>Dogecoin </strong>(CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/doge/usd\">DOGE</a>) did previously.</p>\n\n\n\n<p>Addressing recent rumors and skepticism, Crash dismissed any concerns. </p>\n\n\n\n<p>&#8220;What FUD? I don't see any. All I see is a coin that's pumping into the billions and making people rich,&#8221; he asserted, showcasing his unwavering belief in BRETT&#8217;s potential.</p>\n\n\n\n<p>On BRETT&#8217;s potential to become a top-tier meme coin, Crash was unequivocal. </p>\n\n\n\n<p>&#8220;BRETT is a top-tier meme. Last cycle we had DOGE run to $80 billion and then SHIB to $40 billion. This cycle, I think we will see PEPE run to $80 billion+ and then BRETT will follow as the SHIB to PEPE,&#8221; he predicted.</p>\n\n\n\n<p>For those considering investing in meme coins, Crash offered strategic advice. </p>\n\n\n\n<p>&#8220;Better to go in with size where you know you are gonna win. Most people gamble away all their money on trash hoping to win. BRETT I KNOW is gonna win,&#8221; he exclaimed.</p>\n\n\n\n<p>He likened investing in top meme coins on emerging blockchains to early investments in companies like Tesla or Amazon, emphasizing the importance of making confident, sizeable bets.</p>\n\n\n\n<p>Crash concluded with a strong endorsement of BRETT&#8217;s future. </p>\n\n\n\n<p>&#8220;I&#8217;m confident in BRETT&#8217;s future as the #1 meme on Base and think that BRETT at 7 cents today is the equivalent to buying <strong>Bitcoin </strong>(CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/btc/usd\">BTC</a>) at $700,&#8221; he said, drawing a parallel to the early days of Bitcoin&#8217;s meteoric rise.</p>\n\n\n\n<p><strong>What&#8217;s Next</strong>: These insights into BRETT and the evolving meme coin market will be a focal point at Benzinga&#8217;s <a href=\"https://www.benzinga.com/events/digital-assets/agenda/\">Future of Digital Assets</a> event on Nov. 19, where industry leaders will explore the latest trends and the future of digital asset investments.</p>\n\n\n\n<p><em>Read Next: <a href=\"https://www.benzinga.com/markets/cryptocurrency/24/05/39063040/ripple-donates-additional-25m-to-pro-crypto-super-pac\">Ripple Donates Additional $25M To Pro-Crypto Super PAC</a></em></p>\n\n\n\n<p><em>Image created using artificial intelligence with Midjourney.</em></p>    ",
      "created_at": "2024-05-29T19:20:02Z",
      "headline": "EXCLUSIVE: Can BRETT Become The Shiba Inu Of The Base Blockchain?",
      "id": 39072128,
      "images": [
        {
          "size": "large",
          "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2024/05/29/brett-memecoin.png"
        },
        {
          "size": "small",
          "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2024/05/29/brett-memecoin.png"
        },
        {
          "size": "thumb",
          "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2024/05/29/brett-memecoin.png"
        }
      ],
      "source": "benzinga",
      "summary": "BRETT (CRYPTO: BRETT), a meme coin inspired by the character of the same name from the popular comic series “Boys Club,” is aiming to becom",
      "symbols": [
        "BTCUSD",
        "DOGEUSD",
        "ETHUSD",
        "PEPEUSD",
        "SHIBUSD",
        "SOLUSD"
      ],
      "updated_at": "2024-05-29T19:20:04Z",
      "url": "https://www.benzinga.com/markets/cryptocurrency/24/05/39072128/exclusive-can-brett-become-the-shiba-inu-of-the-base-blockchain"
    },
    {
      "author": "Benzinga Newsdesk",
      "content": "",
      "created_at": "2024-05-29T19:12:43Z",
      "headline": "Apple Signals It's Working On TV+ App For Android Phones; Seeks Senior Android Engineer To Help Build New App",
      "id": 39071954,
      "images": [],
      "source": "benzinga",
      "summary": "",
      "symbols": [
        "AAPL",
        "GOOGL"
      ],
      "updated_at": "2024-05-29T19:12:44Z",
      "url": "https://www.benzinga.com/news/24/05/39071954/apple-signals-its-working-on-tv-app-for-android-phones-seeks-senior-android-engineer-to-help-build-n"
    },
    {
      "author": "Kenneth Rapoza",
      "content": "<p>Key points:</p>\r\n\r\n<ul>\r\n\t<li>The Layer 2 blockchain investor theme has had mixed results over the last 12 months, with Ethereum&rsquo;s Dencun solution underwhelming.</li>\r\n\t<li>Players like Prometeus are near-BTC levels, while giants like Arbitrum are down 13%. It&#39;s only matter of time before there is a flip in fortunes for these beat-up tokens.</li>\r\n</ul>\r\n\r\n<p>A handful of leading so-called &ldquo;Layer 2&rdquo; (or L2) blockchain protocols are not that far away from <strong>Bitcoin&rsquo;s</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/btc/usd\">BTC</a>) 12-month romp of the market.&nbsp; The question is whether those that have tracked Bitcoin&rsquo;s 144%&nbsp; gains over the last year can continue tracking the granddaddy of all cryptocurrencies, or if investors are going to give the laggards their turn next.</p>\r\n\r\n<p>Two of the top performers over the last year are <strong>Prometeus</strong> (CRYPTO:PROM) &ndash; up 146.52% since last May 28 mid-morning trading &ndash; and <strong>Mantle</strong> (MNT), which is up 112.91%. By comparison, traditional stock investors that just bought the <strong>Invesco QQQ Trust</strong> (<a href=\"https://www.benzinga.com/quote/QQQ\" style=\"color:#467886; text-decoration:underline\">QQQ</a>) are up 31.67%.</p>\r\n\r\n<p>Digital asset fund managers have watched the Layer 2 theme for at least the last two years. The idea became more commonplace around 2022-23 for Ethereum users, thanks to L2 developer OP Labs. At the time, <strong>Ethereum</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/eth/usd\">ETH</a>) founder <strong>Vatalik Buterin</strong> was being hounded by blockchain application developers for its speed, or lack thereof, and its cost. A second layer, if you will, developed by alternative blockchains and even Ethereum itself, would help speed things up.</p>\r\n\r\n<p>This opened up the alternative blockchain space, led by giants like <strong>Arbitrum</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/\">ARB</a>), a three billion market cap company now, <a href=\"https://coinmarketcap.com/currencies/arbitrum/\">according to CoinMarketCap</a>. ARB is down year-to-date after a total reversal of fortunes versus BTC this past winter. It&#39;s headed south since March, but if the cryptocurrency bull market has any legs, ARB could close that gap.</p>\r\n\r\n<p><strong>The L2 Investment Case</strong></p>\r\n\r\n<p>The Layer 2 companies all build from <a href=\"https://www.benzinga.com/markets/cryptocurrency/22/07/28203490/scaling-blockchains-what-are-layer-2-solutions-and-interoperable-chains\" style=\"color:#467886; text-decoration:underline\">three different solutions</a>. The solution options are designed to tackle Layer 1 blockchain problems such as speed, cost, and scalability on the blockchain while being able to maintain an open, decentralized, and secure network.&nbsp; This, of course, is easier said than done.</p>\r\n\r\n<p>One way to describe the speed differential between new technologies (blockchains) and old payment systems like Visa, is that Ethereum can process around 7-15 transactions a second. Visa can do around 100,000. Layer 2 technologies are supposed to eventually bring these blockchains up to speed, giving them commercial application. That&rsquo;s been the future play all along for investors, be it venture capitalists funding PROM, or retailers with a crypto trading account.</p>\r\n\r\n<p>Of those three L2 solutions &ndash; ZK-rollups, Optimism rollups, and channels &ndash; ZK-rollups is focused on speed and is the one garnering the most investor attention. Each solution tends to tackle a different problem, and no one has developed a system yet that solves all the concerns of the blockchain community &ndash; be it decentralization versus centralization, or scalability and speed.</p>\r\n\r\n<p>In a sense, these techies, all of whom speak a language that sounds like something out of Battlestar Galactica, and who seem to be maybe 20 years ahead of their time, are trying to create a different internet. Today, the transactions on this new internet, aka Web3, are done in cryptocurrencies lay investors have been piling into for years.</p>\r\n\r\n<p>&ldquo;The number of users acquainted with blockchain&#39;s benefits grows each year,&rdquo; said <strong>Iva Wisher</strong>, co-founder and COO of PROM. &ldquo;These L2 solutions are the key to unlocking the full potential of the blockchain ecosystem. They address the existing limits that L1 networks face. By enhancing accessibility, efficiency, and convenience, these solutions pave the way for further adoption and growth.&rdquo;</p>\r\n\r\n<p>PROM allows developers to be able to connect both to Ethereum network-compatible blockchains and non-Ethereum ones, such as Bitcoin or <strong>Solana</strong> (<a href=\"https://www.benzinga.com/quote/SOL-USD\" style=\"color:#467886; text-decoration:underline\">SOL</a>). This attracts the decentralization aspect of the blockchain developer crowd and mitigates the risk of network downtime. Investors seem to like it this year. Although PROM is down around $50 per coin from its all-time high of $65.86 reached on April 30, 2021, PROM&#39;s first trading day back in 2019 had an initial price of $0.33 and is currently priced a little over $10.</p>\r\n\r\n<p>&ldquo;Ethereum, with its average 12-second block speed, stands out as one of the slowest and most costly around,&rdquo; said <strong>Yves La Rose</strong>, Co-Founder and CEO of <strong>EOS Network Foundation</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/eos/usd\">EOS</a>). &ldquo;It&rsquo;s the layer 2 solutions that allow for substantial enhancements in speed and cost-efficiency, because making those improvements directly on the Ethereum main chain would be a highly contentious issue.&rdquo;</p>\r\n\r\n<p>L2 investors tend to buy the coins of the alternative blockchains, even though Ethereum is still the biggest.</p>\r\n\r\n<p>ETH&rsquo;s first-quarter trading volume dipped under 40%. Analysts have attributed ETH&rsquo;s volume drop during the BTC bull rally to investors following developers to alternative blockchains.</p>\r\n\r\n<p>&ldquo;Competing chains provide options that resonate with crypto lovers disillusioned with Ethereum&rsquo;s offerings,&rdquo; said Elizabeth Kerr, a crypto investment analyst with BanklessTimes. &ldquo;The team at ETH will look at these numbers as a wake-up call,&rdquo; she said.</p>\r\n\r\n<p>In March, Buterin announced that one of its L2 solutions, called <a href=\"https://cointelegraph.com/news/ethereum-ecosystem-mindshift-vitalik-buterin\" style=\"color:#467886; text-decoration:underline\">Dencun</a>, was underwhelming. &ldquo;The amount of usage is interestingly low,&rdquo; he <a href=\"https://decrypt.co/222767/ethereum-founder-vitalik-buterin-surprised-l2-usage-dencun\" style=\"color:#467886; text-decoration:underline\">said</a>.</p>\r\n\r\n<p>Almost all of the blockchain players &ndash; including EOS down 8.9% since last year -- have slipped away from the BTC rally in April.</p>\r\n\r\n<p>But at some point, Bitcoin outperformance will likely flip. The question is whether the laggards like EOS and even L2 solution<strong> Polygon</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/matic/usd\">MATIC</a>), down 19.5%, will reverse course.</p>\r\n\r\n<p class=\"contributor-disclaimer\"><em>This article is from an unpaid external contributor. It does not represent Benzinga&#39;s reporting and has not been edited for content or accuracy.</em></p>\r\n ",
      "created_at": "2024-05-29T18:07:29Z",
      "headline": "Layer 2 Blockchains Like Prometeus, Mantle, Nearly Equal Bitcoin Gains. But Are The L2 Players Worth The Investor Risk Now?",
      "id": 39070900,
      "images": [
        {
          "size": "large",
          "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/-_2_7.jpg"
        },
        {
          "size": "small",
          "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/-_2_7.jpg"
        },
        {
          "size": "thumb",
          "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/-_2_7.jpg"
        }
      ],
      "source": "benzinga",
      "summary": "Key points:",
      "symbols": [
        "ARBUSD",
        "BTCUSD",
        "EOSUSD",
        "ETHUSD",
        "MATICUSD"
      ],
      "updated_at": "2024-05-29T18:08:18Z",
      "url": "https://www.benzinga.com/24/05/39070900/layer-2-blockchains-like-prometeus-mantle-nearly-equal-bitcoin-gains-but-are-the-l2-players-worth-th"
    },
    {
      "author": "Chris Katje",
      "content": "<p><strong>Tesla Inc</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/TSLA#NASDAQ\">TSLA</a>) CEO <strong>Elon Musk </strong>has had a contentious relationship with President <strong>Joe Biden </strong>and <a href=\"https://www.benzinga.com/markets/equities/24/05/38910114/elon-musk-counts-amazing-president-joe-biden-among-tesla-naysayers-who-wish-to-see-the-ev-maker-\">the current White House administration.</a></p>\n\n\n\n<p>While Biden has been pro-electric vehicle (EV), his strong pro-union policies have also angered Musk.</p>\n\n\n\n<p><strong>What Happened:</strong> Musk has not endorsed <strong>Donald Trump</strong> in <a href=\"https://www.benzinga.com/topic/2024-election\">the 2024 election</a>, but has said that he is<a href=\"https://www.benzinga.com/general/social-media/24/03/37722839/elon-musk-uncommitted-in-biden-trump-race-reveals-who-hes-leaning-away-from\"> leaning away</a> from Biden, the candidate he said he voted for in the 2020 presidential election.</p>\n\n\n\n<p>If Trump wins the 2024 election, Musk could find himself in a new advisory role.</p>\n\n\n\n<p>Musk and Trump have discussed the potential role in the event of Trump being re-elected to the presidency, as <a href=\"https://www.wsj.com/politics/donald-trump-elon-musk-alliance-d1fe43e3\">reported </a>by The Wall Street Journal.</p>\n\n\n\n<p>Along with potential influence on policies related to electric vehicles, Musk could also be used for input on border security, technology, science, space exploration, and the economy, according to the report.</p>\n\n\n\n<p>The report said Musk developed a plan to prevent voter fraud alongside investor <strong>Nelson Peltz</strong> that was presented to Trump.</p>\n\n\n\n<p>The two parties speak on the phone directly, according to the report. Previous reports linked Musk and Trump meeting in March, which Musk has since downplayed.</p>\n\n\n\n<p>\"I was at a breakfast at a friend's place and Donald Trump came by, that's it,\" Musk told <strong>Don Lemon</strong> in an interview.</p>\n\n\n\n<p>Musk said he can't remember what the two discussed and that Trump \"did most of the talking.\"</p>\n\n\n\n<p>The new report from the WSJ says Musk and Trump met in March at Peltz's Florida estate, where the advisory role was discussed.</p>\n\n\n\n<p><em>Related Link:<a href=\"https://www.benzinga.com/markets/equities/24/05/39063828/elon-musk-slams-joe-biden-says-president-cares-a-lot-more-about-whether-tesla-is-unionized-over-\"> Elon Musk Slams Joe Biden, Says President &#8216;Cares A Lot More About Whether Tesla Is Unionized&#8217; Over EV Maker&#8217;s Environmental Impact</a></em></p>\n\n\n\n<p><strong>Why It's Important</strong>: Trump and Musk have not always seen eye to eye on many items and frequently have traded insults at each other across social media. </p>\n\n\n\n<p>Musk has also <a href=\"https://www.benzinga.com/news/small-cap/22/04/26850021/elon-musk-takes-a-shot-at-twitter-and-truth-social\">been critical of</a> <strong>Truth Social,</strong> which is owned by <strong>Trump Media &amp; Technology</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/DJT#NASDAQ\">DJT</a>). Trump tried to get Musk to acquire the social media platform previously, according to <a href=\"https://www.benzinga.com/general/politics/24/03/37625748/trump-tried-to-get-elon-musk-to-buy-truth-social-new-report-highlights-former-presidents-pitch\">a past report</a> from The Washington Post.</p>\n\n\n\n<p>Trump has spoken out about electric vehicles in the past and recently reportedly tried to <a href=\"https://www.benzinga.com/news/24/05/38997165/trumps-policies-for-money-transaction-with-big-oil-under-investigation-by-senate-democrats-cronyism\">cozy up to big oil companies</a> in a campaign donation plan that would role back several environmental policies.</p>\n\n\n\n<p>Musk previously served on business advisory groups during Trump's first presidential term. He later resigned in 2017 after a disagreement on Trump pulling the U.S. out of the Paris climate accord.</p>\n\n\n\n<p>The Tesla CEO, who also owns the X social media platform, unbanned Trump from the platform, but Trump has only made one post since returning. Musk has said he wants to see Trump use X more, including the Spaces live audio feature for items<a href=\"https://www.benzinga.com/news/24/05/38865604/elon-musk-calls-for-hosting-biden-vs-trump-debate-on-x-as-race-to-white-house-gains-momentum\"> like presidential debates.</a></p>\n\n\n\n<p>While discussions on the role could fall apart and they center on Trump being elected, the fact that Musk is being considered could show how Musk and Trump rebuilt their relationship and could lead to Trump pushing for a public endorsement from the well-known and often followed billionaire.</p>\n\n\n\n<p><em>Read Next: <a href=\"http://Elon Musk Slams Biden Administration Over 100% Tariffs On Chinese EV Imports: 'Things That...Distort The Market Are Not Good'\">Elon Musk Slams Biden Administration Over 100% Tariffs On Chinese EV Imports: &#8216;Things That&#8230; Distort The Market Are Not Good&#8217;</a></em></p>\n\n\n\n<p><em>Image: Shutterstock</em></p>",
      "created_at": "2024-05-29T17:36:35Z",
      "headline": "Elon Musk In The White House? Tesla CEO Could Land Advisory Role For Donald Trump: Report",
      "id": 39070289,
      "images": [
        {
          "size": "large",
          "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2024/05/29/Elon-Musk-and-Donald-Trump-Photos-by-Fre.jpeg"
        },
        {
          "size": "small",
          "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2024/05/29/Elon-Musk-and-Donald-Trump-Photos-by-Fre.jpeg"
        },
        {
          "size": "thumb",
          "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2024/05/29/Elon-Musk-and-Donald-Trump-Photos-by-Fre.jpeg"
        }
      ],
      "source": "benzinga",
      "summary": "Elon Musk could be an advisor to Donald Trump in a new role if the former president wins the 2024 election.",
      "symbols": [
        "DJT",
        "TSLA"
      ],
      "updated_at": "2024-05-29T17:36:36Z",
      "url": "https://www.benzinga.com/general/politics/24/05/39070289/elon-musk-in-the-white-house-tesla-ceo-could-land-advisory-role-for-donald-trump-report"
    },
    {
      "author": "Benzinga Insights",
      "content": "<p>This whale alert can help traders discover the next big trading opportunities.</p>\n<p>Whales are entities with large sums of money and we track their transactions here at Benzinga on our options activity scanner.</p>\n<p>Traders often look for circumstances when the market estimation of an option diverges away from its normal worth. Abnormal amounts of trading activity could push option prices to hyperbolic or underperforming levels. </p>\n<p>Below are some instances of options activity happening in the Consumer Discretionary sector:  <table>\n<thead>\n<tr>\n<th><strong>Symbol</strong></th>\n<th><strong>PUT/CALL</strong></th>\n<th><strong>Trade Type</strong></th>\n<th><strong>Sentiment</strong></th>\n<th><strong>Exp. Date</strong></th>\n<th><strong>Strike Price</strong></th>\n<th><strong>Total Trade Price</strong></th>\n<th><strong>Open Interest</strong></th>\n<th><strong>Volume</strong></th>\n</tr>\n</thead>\n<tbody>\n<tr>\n<td>TSLA</td>\n<td>CALL</td>\n<td>TRADE</td>\n<td>BEARISH</td>\n<td>05/31/24</td>\n<td>$177.50</td>\n<td>$47.6K</td>\n<td>10.8K</td>\n<td>90.4K</td>\n</tr>\n<tr>\n<td>DKS</td>\n<td>PUT</td>\n<td>TRADE</td>\n<td>BEARISH</td>\n<td>07/19/24</td>\n<td>$170.00</td>\n<td>$186.4K</td>\n<td>5.4K</td>\n<td>5.1K</td>\n</tr>\n<tr>\n<td>BABA</td>\n<td>CALL</td>\n<td>SWEEP</td>\n<td>BULLISH</td>\n<td>06/14/24</td>\n<td>$85.00</td>\n<td>$39.3K</td>\n<td>2.9K</td>\n<td>3.7K</td>\n</tr>\n<tr>\n<td>PENN</td>\n<td>CALL</td>\n<td>TRADE</td>\n<td>BEARISH</td>\n<td>06/21/24</td>\n<td>$17.50</td>\n<td>$39.3K</td>\n<td>13.1K</td>\n<td>3.4K</td>\n</tr>\n<tr>\n<td>W</td>\n<td>CALL</td>\n<td>SWEEP</td>\n<td>BULLISH</td>\n<td>07/19/24</td>\n<td>$50.00</td>\n<td>$55.1K</td>\n<td>79</td>\n<td>1.5K</td>\n</tr>\n<tr>\n<td>JD</td>\n<td>CALL</td>\n<td>SWEEP</td>\n<td>NEUTRAL</td>\n<td>06/07/24</td>\n<td>$30.00</td>\n<td>$39.6K</td>\n<td>265</td>\n<td>1.0K</td>\n</tr>\n<tr>\n<td>CAVA</td>\n<td>CALL</td>\n<td>SWEEP</td>\n<td>BULLISH</td>\n<td>06/21/24</td>\n<td>$80.00</td>\n<td>$25.1K</td>\n<td>849</td>\n<td>717</td>\n</tr>\n<tr>\n<td>ANF</td>\n<td>CALL</td>\n<td>SWEEP</td>\n<td>BULLISH</td>\n<td>05/31/24</td>\n<td>$175.00</td>\n<td>$39.0K</td>\n<td>639</td>\n<td>613</td>\n</tr>\n<tr>\n<td>BOOT</td>\n<td>PUT</td>\n<td>SWEEP</td>\n<td>BULLISH</td>\n<td>06/21/24</td>\n<td>$110.00</td>\n<td>$74.3K</td>\n<td>655</td>\n<td>500</td>\n</tr>\n<tr>\n<td>GME</td>\n<td>PUT</td>\n<td>SWEEP</td>\n<td>BEARISH</td>\n<td>07/19/24</td>\n<td>$20.00</td>\n<td>$85.0K</td>\n<td>8.2K</td>\n<td>358</td>\n</tr>\n</tbody>\n</table></p>\n<h2>Explanation</h2>\n<p>These itemized elaborations have been created using the accompanying table.  </p>\n<p>•  For <strong>TSLA</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/TSLA#NASDAQ\">TSLA</a>), we notice a <strong>call</strong> option <strong>trade</strong> that happens to be <strong>bearish</strong>, expiring in 2 day(s) on <strong>May 31, 2024</strong>. This event was a transfer of <strong>200</strong> contract(s) at a <strong>$177.50</strong> strike. The total cost received by the writing party (or parties) was <strong>$47.6K</strong>, with a price of <strong>$238.0</strong> per contract. There were <strong>10839</strong> open contracts at this strike prior to today, and today <strong>90449</strong> contract(s) were bought and sold. </p>\n<p>•  For <strong>DKS</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/DKS#NYSE\">DKS</a>), we notice a <strong>put</strong> option <strong>trade</strong> that happens to be <strong>bearish</strong>, expiring in 51 day(s) on <strong>July 19, 2024</strong>. This event was a transfer of <strong>4144</strong> contract(s) at a <strong>$170.00</strong> strike. The total cost received by the writing party (or parties) was <strong>$186.4K</strong>, with a price of <strong>$45.0</strong> per contract. There were <strong>5456</strong> open contracts at this strike prior to today, and today <strong>5103</strong> contract(s) were bought and sold. </p>\n<p>•  For <strong>BABA</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/BABA#NYSE\">BABA</a>), we notice a <strong>call</strong> option <strong>sweep</strong> that happens to be <strong>bullish</strong>, expiring in 16 day(s) on <strong>June 14, 2024</strong>. This event was a transfer of <strong>530</strong> contract(s) at a <strong>$85.00</strong> strike. This particular call needed to be split into 4 different trades to become filled. The total cost received by the writing party (or parties) was <strong>$39.3K</strong>, with a price of <strong>$74.0</strong> per contract. There were <strong>2936</strong> open contracts at this strike prior to today, and today <strong>3776</strong> contract(s) were bought and sold. </p>\n<p>•  For <strong>PENN</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/PENN#NASDAQ\">PENN</a>), we notice a <strong>call</strong> option <strong>trade</strong> that happens to be <strong>bearish</strong>, expiring in 23 day(s) on <strong>June 21, 2024</strong>. This event was a transfer of <strong>2187</strong> contract(s) at a <strong>$17.50</strong> strike. The total cost received by the writing party (or parties) was <strong>$39.3K</strong>, with a price of <strong>$18.0</strong> per contract. There were <strong>13136</strong> open contracts at this strike prior to today, and today <strong>3453</strong> contract(s) were bought and sold. </p>\n<p>•  Regarding <strong>W</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/W#NYSE\">W</a>), we observe a <strong>call</strong> option <strong>sweep</strong> with <strong>bullish</strong> sentiment. It expires in 51 day(s) on <strong>July 19, 2024</strong>. Parties traded <strong>56</strong> contract(s) at a <strong>$50.00</strong> strike. This particular call needed to be split into 21 different trades to become filled. The total cost received by the writing party (or parties) was <strong>$55.1K</strong>, with a price of <strong>$985.0</strong> per contract. There were <strong>79</strong> open contracts at this strike prior to today, and today <strong>1566</strong> contract(s) were bought and sold. </p>\n<p>•  For <strong>JD</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/JD#NASDAQ\">JD</a>), we notice a <strong>call</strong> option <strong>sweep</strong> that happens to be <strong>neutral</strong>, expiring in 9 day(s) on <strong>June 7, 2024</strong>. This event was a transfer of <strong>650</strong> contract(s) at a <strong>$30.00</strong> strike. This particular call needed to be split into 3 different trades to become filled. The total cost received by the writing party (or parties) was <strong>$39.6K</strong>, with a price of <strong>$61.0</strong> per contract. There were <strong>265</strong> open contracts at this strike prior to today, and today <strong>1026</strong> contract(s) were bought and sold. </p>\n<p>•  Regarding <strong>CAVA</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/CAVA#NYSE\">CAVA</a>), we observe a <strong>call</strong> option <strong>sweep</strong> with <strong>bullish</strong> sentiment. It expires in 23 day(s) on <strong>June 21, 2024</strong>. Parties traded <strong>34</strong> contract(s) at a <strong>$80.00</strong> strike. This particular call needed to be split into 3 different trades to become filled. The total cost received by the writing party (or parties) was <strong>$25.1K</strong>, with a price of <strong>$740.0</strong> per contract. There were <strong>849</strong> open contracts at this strike prior to today, and today <strong>717</strong> contract(s) were bought and sold. </p>\n<p>•  Regarding <strong>ANF</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/ANF#NYSE\">ANF</a>), we observe a <strong>call</strong> option <strong>sweep</strong> with <strong>bullish</strong> sentiment. It expires in 2 day(s) on <strong>May 31, 2024</strong>. Parties traded <strong>30</strong> contract(s) at a <strong>$175.00</strong> strike. This particular call needed to be split into 5 different trades to become filled. The total cost received by the writing party (or parties) was <strong>$39.0K</strong>, with a price of <strong>$1300.0</strong> per contract. There were <strong>639</strong> open contracts at this strike prior to today, and today <strong>613</strong> contract(s) were bought and sold. </p>\n<p>•  Regarding <strong>BOOT</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/BOOT#NYSE\">BOOT</a>), we observe a <strong>put</strong> option <strong>sweep</strong> with <strong>bullish</strong> sentiment. It expires in 23 day(s) on <strong>June 21, 2024</strong>. Parties traded <strong>338</strong> contract(s) at a <strong>$110.00</strong> strike. This particular put needed to be split into 88 different trades to become filled. The total cost received by the writing party (or parties) was <strong>$74.3K</strong>, with a price of <strong>$220.0</strong> per contract. There were <strong>655</strong> open contracts at this strike prior to today, and today <strong>500</strong> contract(s) were bought and sold. </p>\n<p>•  Regarding <strong>GME</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/GME#NYSE\">GME</a>), we observe a <strong>put</strong> option <strong>sweep</strong> with <strong>bearish</strong> sentiment. It expires in 51 day(s) on <strong>July 19, 2024</strong>. Parties traded <strong>200</strong> contract(s) at a <strong>$20.00</strong> strike. This particular put needed to be split into 3 different trades to become filled. The total cost received by the writing party (or parties) was <strong>$85.0K</strong>, with a price of <strong>$425.0</strong> per contract. There were <strong>8209</strong> open contracts at this strike prior to today, and today <strong>358</strong> contract(s) were bought and sold. </p>\n<p><strong>Options Alert Terminology</strong><br />\n - <strong>Call Contracts:</strong> The right to buy shares as indicated in the contract.<br />\n - <strong>Put Contracts:</strong> The right to sell shares as indicated in the contract.<br />\n - <strong>Expiration Date:</strong> When the contract expires. One must act on the contract by this date if one wants to use it.<br />\n - <strong>Premium/Option Price:</strong> The price of the contract.  </p>\n<p>For more information, visit our <em><a href=\"https://pro.benzinga.com/blog/how-to-understand-option-alerts/\">Guide to Understanding Options Alerts</a></em> or read <a href=\"https://www.benzinga.com/markets/options\">more news on unusual options activity</a>.  </p>\n<p>This article was generated by Benzinga's automated content engine and reviewed by an editor.</p>",
      "created_at": "2024-05-29T17:35:18Z",
      "headline": "10 Consumer Discretionary Stocks Whale Activity In Today's Session",
      "id": 39070273,
      "images": [
        {
          "size": "large",
          "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2023/options_image_4.jpeg"
        },
        {
          "size": "small",
          "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2023/options_image_4.jpeg"
        },
        {
          "size": "thumb",
          "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2023/options_image_4.jpeg"
        }
      ],
      "source": "benzinga",
      "summary": " ",
      "symbols": [
        "ANF",
        "BABA",
        "BOOT",
        "CAVA",
        "DKS",
        "GME",
        "JD",
        "PENN",
        "TSLA",
        "W"
      ],
      "updated_at": "2024-05-29T17:35:19Z",
      "url": "https://www.benzinga.com/insights/options/24/05/39070273/10-consumer-discretionary-stocks-whale-activity-in-todays-session"
    },
    {
      "author": "Piero Cingari",
      "content": "<p>Volatility surged back into the market on Wednesday, with the CBOE Volatility Index (VIX) spiking 9% after hitting nearly three-year lows last week, fueled by fresh upticks <a href=\"https://www.benzinga.com/24/05/39066480/vix-rises-8-treasury-yields-jump-dow-plunges-why-is-wall-street-wobbling-thursday\">in Treasury bond yields.</a></p>\n\n\n\n<p>The yield on the 30-year Treasury note, a crucial benchmark for mortgage rates nationwide, soared to 4.74%, rising more than 15 basis points over two sessions and nearing its highest close since May 2.</p>\n\n\n\n<p>As yields climbed, bond prices dropped, with the <strong>iShares 20+ Year Treasury Bond ETF</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/TLT#NASDAQ\">TLT</a>) falling 1.3%, following a 1.4% decline on Tuesday.</p>\n\n\n\n<p>Investors fear that the Fed will not cut interest rates more than once by the end of the year and not before November, as suggested by current Fed futures pricing.</p>\n\n\n\n<p>All major U.S. equity indices and all eleven sectors traded in the red, on a day when the U.S. dollar effectively played its safe haven role. The <strong>Invesco DB USD Index Bullish Fund ETF</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/UUP#NYSE\">UUP</a>) rose 0.5%, marking its strongest day in a month.</p>\n\n\n\n<p>Rising yields and a stronger dollar pressured commodities, with gold prices down 1%, oil down 1.3%, and natural gas down 5%.</p>\n\n\n\n<p><strong>Bitcoin</strong> (CRYPTO: <a class=\"ticker\" href=\"https://www.benzinga.com/quote/btc/usd\">BTC</a>) dropped 1.5%, echoing Tuesday&#8217;s decline.</p>\n\n\n\n<h3 class=\"wp-block-heading\">Wednesday&#8217;s Performance In Major US Indices, ETFs</h3>\n\n\n\n<figure class=\"wp-block-table is-style-stripes\"><table><tbody><tr><td><strong>Major Indices</strong></td><td><strong>Price</strong></td><td><strong>1-day %Chg </strong></td></tr><tr><td>Nasdaq 100</td><td>18,812.28</td><td>-0.3%</td></tr><tr><td>S&amp;P 500</td><td>5,281.15</td><td>-0.5%</td></tr><tr><td>Dow Jones</td><td>38,512.75</td><td>-0.9%</td></tr><tr><td>Russell 2000</td><td>2,040.63</td><td>-1.2%</td></tr></tbody></table><figcaption class=\"wp-element-caption\"><em>Updated at 12:35 p.m. EDT</em></figcaption></figure>\n\n\n\n<p>According to <a href=\"https://pro.benzinga.com/dashboard\">Benzinga Pro data</a>:</p>\n\n\n\n<ul>\n<li>The <strong>SPDR S&amp;P 500 ETF Trust</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/SPY#NYSE\">SPY</a>) was 0.6% lower to $526.92</li>\n\n\n\n<li>The <strong>SPDR Dow Jones Industrial Average</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/DIA#NYSE\">DIA</a>) fell 0.9% to $385.15</li>\n\n\n\n<li>The tech-heavy <strong>Invesco QQQ Trust</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/QQQ#NASDAQ\">QQQ</a>) was down by 0.4% to $457.81</li>\n\n\n\n<li>The <strong>Communication Services</strong> <strong>Select Sector SPDR Fund</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/XLC#NYSE\">XLC</a>) minimized losses, down by 0.2%. </li>\n\n\n\n<li>The <strong>Energy Select Sector SPDR Fund</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/XLE#NYSE\">XLE</a>) lagged, easing 1.7%.</li>\n</ul>\n\n\n\n<h3 class=\"wp-block-heading\">Wednesday&#8217;s Stock Movers</h3>\n\n\n\n<ul>\n<li><strong>American Airlines Group Inc.</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/AAL#NYSE\">AAL</a>) tumbled 14%, on track for the worst-performing day since March 2020, after the airline company trimmed its Q2 earnings guidance. Additionally, AAL suffered analyst downgrades from Jefferies and Seaport Global.</li>\n\n\n\n<li><strong>ConocoPhillips</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/COP#NYSE\">COP</a>) will buy <strong>Marathon Oil Corp.</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/MRO#NYSE\">MRO</a>) in an all-stock deal worth $22.5 billion, implying a 14% premium for Tuesday&#8217;s close. Shares of ConocoPhillips fell 4%, while MRO rose 8% only. </li>\n\n\n\n<li><strong>Bank OZK</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/OZK#NASDAQ\">OZK</a>) plummeted 14%, eyeing the sharpest decline since Mar. 19, 2020, as Citigroup downgrade the stock from Buy to Sell, citing substantial concerns on two of the bank&#8217;s largest loans. </li>\n\n\n\n<li><strong>Dicks Sporting Goods Inc.</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/DKS#NYSE\">DKS</a>) spiked 15% after the company largely beat Street&#8217;s earnings and revenue expectations. </li>\n\n\n\n<li>Other stocks reacting to corporate earnings were <strong>Heico Corp. </strong>(NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/HEI#NYSE\">HEI</a>) up 2.1%,<strong> Viking Holdings Ltd</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/VIK#NYSE\">VIK</a>) down 2.7%, <strong>Chewy Inc.</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/CHWY#NYSE\">CHWY</a>) up 29%, <strong>Abercrombie &amp; Fitch Company</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/ANF#NYSE\">ANF</a>) 22%, <strong>Advance Auto Parts Inc.</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/AAP#NYSE\">AAP</a>) down 8%. </li>\n\n\n\n<li>Companies reporting earnings after the close include <strong>Salesforce Inc.</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/CRM#NYSE\">CRM</a>), <strong>Agilent Technologies Inc</strong>. (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/A#NYSE\">A</a>), <strong>HP Inc</strong>. (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/HPQ#NYSE\">HPQ</a>), <strong>Pure Storage Inc.</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/PSTG#NYSE\">PSTG</a>), Nutanix Inc. (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/NTNX#NASDAQ\">NTNX</a>), <strong>Okta Inc.</strong> (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/OKTA#NASDAQ\">OKTA</a>), <strong>Ui Path Inc.</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/PATH#NYSE\">PATH</a>) and <strong>Capri Holdings Ltd</strong> (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/CPRI#NYSE\">CPRI</a>). </li>\n</ul>\n\n\n\n<p><em>Now Read:</em> <em><a href=\"https://www.benzinga.com/analyst-ratings/analyst-color/24/05/39068979/how-to-trade-us-elections-a-trump-victory-is-likely-to-lead-to-a-stronger-dollar\">How To Trade US Elections: &#8216;A Trump Victory Is Likely To Lead To A Stronger Dollar&#8217;</a></em></p>\n\n\n\n<p><em>Image: Pixabay</em></p>    ",
      "created_at": "2024-05-29T17:32:49Z",
      "headline": "Volatility Spooks Investors As Treasury Yields, Dollar Climb Ahead Of Key Economic Releases: What's Driving Markets Wednesday?",
      "id": 39070214,
      "images": [
        {
          "size": "large",
          "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2024/05/29/reports-earnings_0.jpeg"
        },
        {
          "size": "small",
          "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2024/05/29/reports-earnings_0.jpeg"
        },
        {
          "size": "thumb",
          "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2024/05/29/reports-earnings_0.jpeg"
        }
      ],
      "source": "benzinga",
      "summary": "Volatility surged back into the market on Wednesday, with the CBOE Volatility Index (VIX) spiking 9% after hitting nearly three-year lows last week, fueled by fresh upticks in Treasury bond yields.",
      "symbols": [
        "A",
        "AAL",
        "AAP",
        "ANF",
        "BTCUSD",
        "CHWY",
        "COP",
        "CPRI",
        "CRM",
        "DIA",
        "DKS",
        "HEI",
        "HPQ",
        "MRO",
        "NTNX",
        "OKTA",
        "OZK",
        "PATH",
        "PSTG",
        "QQQ",
        "SPY",
        "TLT",
        "UUP",
        "VIK",
        "XLC",
        "XLE",
        "XLV"
      ],
      "updated_at": "2024-05-29T17:32:50Z",
      "url": "https://www.benzinga.com/markets/equities/24/05/39070214/volatility-spooks-investors-as-treasury-yields-dollar-climb-ahead-of-key-economic-releases-whats"
    },
    {
      "author": "Upwallstreet",
      "content": "<p>While legacy automakers General Motors (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/GM#NYSE\">GM</a>) and Ford Motor (NYSE:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/F#NYSE\">F</a>) continue to scale down and reassess their EV ambitions, Hyundai Motor Company (OTC:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/HYMTF#OTC\">HYMTF</a>) is growing its EV portfolio. After setting a strong foundation with its current EV success in the U.S. with IONIQ 5, IONIQ 6 and Kona Electric, Hyundai&nbsp;will be introducing a three-row electric SUV, the IONIQ 9.</p>\r\n\r\n<p>While even the EV king, Tesla Inc (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/TSLA#NASDAQ\">TSLA</a>) kicked off 2024 by struggling with the slowdown, Hyundai has been enjoying increased interest in its EV offerings. During the first quarter, Hyundai reported that its EV sales surged as much as&nbsp;62% due to record performances of the IONIQ 5 and Kona Electric.&nbsp;</p>\r\n\r\n<h3>The IONIQ 9 Promises To Cement Hyundais&rsquo; EV Positioning</h3>\r\n\r\n<p>The Hyundai IONIQ 9 will be Hyundai&rsquo;s first three-row electric SUV. Therefore, it will compete with three row electric SUVs from Rivian Automotive Inc (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/RIVN#NASDAQ\">RIVN</a>), namely the Rivian R1S, as well as Kia Ev9 and Volvo EX90. With the pitch of the IONIQ 9, Hyundai aims to cement its status as a leading provider of affordable and efficient EVs. Moreover, its vehicles will also be enhanced by the world&rsquo;s first solar-tonneau cover thanks to its signed agreement with&nbsp;Worksport Ltd. (NASDAQ:<a class=\"ticker\" href=\"https://www.benzinga.com/stock/WKSP#NASDAQ\">WKSP</a>). Hyundai was the first to express interest in Worksport&rsquo;s revolutionary power duo, the SOLIS solar tonneau cover and the COR portable battery system, whose alpha versions are expected to hit the market this summer.</p>\r\n\r\n<h3>Worksport Has Been Issued A&nbsp;New U.S. Patent For Its Innovative Solar Truck Cover</h3>\r\n\r\n<p>Worksport enlarged its already impressive intellectual property portfolio as the United States Patent &amp; Trademark Office&nbsp;issued new utility patent for its&nbsp;SOLIS solar-powered tonneau cover.&nbsp;Worksport is bringing the world&rsquo;s first solar-powered tonneau truck that promise to disrupt the market which sells about 7 million truck bed covers per year. Earlier this year, Worksport SOLIS cover will be made compatible with the top three selling vehicles in the U.S., namely Ford F-Series, Chevrolet Silverado, and Ram pickup trucks, along with other major brands. Hyundai signed an agreement back in 2022 to ensure it gains access to both SOLIS and COR to empower its pickups. This innovative product, as part of the power duo together with COR portable battery system, will enable Worksport to target both combustion engine pickups, along with OEM integration for upcoming electric pickup trucks, extending their range.</p>\r\n\r\n<p>Along with Ford and GM, even Tesla took a step back. Tesla and Rivian kicked off the year with layoffs. But part of the problem even for Tesla was the lack of new products, with its Model 3 and Model Y being old news, despite the revamping of the Model 3, and the eye-catching Cybertruck not being a mainstream product. Hyundai certainly does not have that problem as it showed its determination to stick to its EV rollout and growth plans.</p>\r\n\r\n<p><em>DISCLAIMER:&nbsp;This content is for informational purposes only. It is not intended as investing advice.</em></p>\r\n\r\n<p class=\"contributor-disclaimer\"><em>This article is from an unpaid external contributor. It does not represent Benzinga&#39;s reporting and has not been edited for content or accuracy.</em></p>\r\n",
      "created_at": "2024-05-29T17:30:07Z",
      "headline": "Hyundai Continues To Expand Its EV Lineup",
      "id": 39070152,
      "images": [
        {
          "size": "large",
          "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/electric-cars-are-being-charged-vehicle-parking-with-solar-panel-energy.jpg"
        },
        {
          "size": "small",
          "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/electric-cars-are-being-charged-vehicle-parking-with-solar-panel-energy.jpg"
        },
        {
          "size": "thumb",
          "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/electric-cars-are-being-charged-vehicle-parking-with-solar-panel-energy.jpg"
        }
      ],
      "source": "benzinga",
      "summary": "While legacy automakers General Motors (NYSE: GM) and Ford Motor (NYSE: F) continue to scale down and reassess their EV ambitions, Hyundai Motor Company (OTC: HYMTF) is growing its EV portfoli",
      "symbols": [
        "F",
        "GM",
        "HYMTF",
        "RIVN",
        "TSLA",
        "WKSP"
      ],
      "updated_at": "2024-05-29T17:32:08Z",
      "url": "https://www.benzinga.com/markets/penny-stocks/24/05/39070152/hyundai-continues-to-expand-its-ev-lineup"
    }
  ],
  "next_page_token": "MTcxNzAwMzkyODAwMDAwMDAwMHwzOTA3MDE1Mg=="
}