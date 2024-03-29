# Year in Review

In an effort to analyze market activity and make use of some of the data I've gathered, this report will delve into the activity of the card market in 2023, as well as make some comparisons to that of 2022.

All of these statistics will be looked at with gifting (trades where the price = 0) and without gifting, as well have their [relevant sql query provided](https://github.com/Kractero/2023/blob/master/Queries.md).

Go to section
- [A Brief Comparison with 2023 and 2022](#a-brief-comparison-with-2023-and-2022)
  - [2023](#2023)
  - [2022](#2022)
  - [Useless Insights](#useless-insights)
- [More Into 2023 Numbers](#more-into-2023-numbers)
  - [Rarities](#2023-rarities)
  - [Seasons](#2023-by-season)
  - [Rarities and Seasons](#season-3-by-both-rarity-and-season)
- [Trades](#trades)
  - [Top Trades](#top-trades-of-the-year)
  - By Rarity
    - [Common](#top-common-trades-of-the-year)
    - [Uncommon](#top-uncommon-trades-of-the-year)
    - [Rare](#top-rare-trades-of-the-year)
    - [Ultra Rare](#top-ultra-rare-trades-of-the-year)
    - [Epic](#top-epic-trades-of-the-year)
    - [Legendary](#top-legendary-trades-of-the-year)
      - [S1](#top-s1-legendary-trades-of-the-year)
  - [Specific Cards](#individual-cards)
      - [Most Moved Card](#most-moved-cards)
      - [Most Bank](#most-money-moved-per-card)
      - [Most Traded Legendary ( > 0 )](#most-traded-legendary)
      - [Most Bank Moved By Legendary](#most-bank-moved-by-legendary)
- [Traders](#buyers-and-sellers)
  - [Bank Movement](#bank-movers)
    - [Most Bank Moved](#most-bank-moved)
      - [As Buyer](#most-bank-moved-as-buyer)
      - [As Seller](#most-bank-moved-as-seller)
    - [Trade Count](#trade-count)
      - [Most Active Trader](#most-active-traders)
      - [Most Active Trader ( > 0 )](#most-active-traders-non-gift-non-zero)
      - [Most Active Buyers](#most-cards-bought)
      - [Most Active Buyers ( > 0 )](#most-cards-bought-for-more-than-zero)
      - [Most Active Sellers](#most-cards-sold)
      - [Most Active Sellers ( > 0 )](#most-cards-sold-for-more-than-zero)
      - [Most Gifts](#most-cards-gifted)
      - [Most Cards Bought at 250+](#most-cards-bought-250)
      - [Most Cards Sold at 250+](#most-cards-sold-250)
    - [Buyers By Season](#buyers-by-season)
      - [S1](#season-1)
      - [S1 ( > 0 )](#season-1-non-zero)
      - [S2](#season-2)
      - [S2 ( > 0 )](#season-2-non-zero)
      - [S3](#season-3)
      - [S3 ( > 0 )](#season-3-non-zero)
    - [Buyers By Rarity ( > 0 )](#buyers-by-rarity-non-zero)
      - [Common](#common)
      - [Uncommon](#uncommon)
      - [Rare](#rare-1)
      - [Ultra Rare](#ultra-rare-1)
      - [Epic](#epic-1)
      - Legendaries
        - [Legendaries](#legendaries-bought)
        - [Legendaries ( > 0 )](#legendaries-bought-non-zero)
        - [Legendaries Gifted](#legendaries-gifted)
        - [Legendaries Received](#legendaries-received)
- [Temporal Stuff](#time-breakdown)
  - Year in Halves
    - [Jan-July](#first-half-of-the-year)
      - [As Buyer](#most-bank-moved-as-buyer)
      - [As Seller](#most-bank-moved-as-seller)
      - [Most Active Buyers](#most-cards-bought-1)
      - [Most Active Buyers ( > 0 )](#most-cards-bought-non-zero)
      - [Most Active Sellers](#most-cards-sold-1)
      - [Most Active Sellers ( > 0 )](#most-cards-sold-non-zero)
    - [July-Jan 2024](#last-half-of-the-year)
      - [As Buyer](#most-bank-moved-as-buyer-1)
      - [As Seller](#most-bank-moved-as-seller-1)
      - [Most Active Buyers](#most-cards-bought-2)
      - [Most Active Buyers ( > 0 )](#most-cards-bought-non-zero-1)
      - [Most Active Sellers](#most-cards-sold-2)
      - [Most Active Sellers ( > 0 )](#most-cards-sold-non-zero-1)
  - [Hours, Days, Months](#hours-days-months)
      - [Most Active Day](#most-active-day)
      - [Hours of the Day](#hour-of-the-day)
      - [Days of the Week](#day-of-the-week)
      - [Months of the Year](#month-of-the-year)
  - [Cards, Traders](#cards-traders)
      - [Top Traders Per Month](#traders-per-month-non-zero)
      - [Most Bank Moved Per Month](#most-bank-moved-per-month)
      - [Unique Cards Sold Per Month](#number-of-unique-cards-traded-each-month)
      - [Top 3 Legendaries By Bank Per Month](#top-3-legendaries-by-bank-each-month)


## A Brief Comparison with 2023 and 2022:

### 2023

The card market in 2023 was very active, numbering at `2,493,179` trades, which saw `3,112,218.81` bank moved between trades.

When gifts are excluded, the market recorded `1,139,606` trades, or 45.7% of all trades. The average trade value within these non-gifts were `2.73` bank.

The market also saw a total of 72,061 unique nations purchase a card, 116,020 unique nations sell a card, and a total of 126,660 nations participate in the market as a whole.

In 2023, there were over `947` trades that occured with a value of over 250, with `738` between 250 and 499 and `209` at over 500.

- Total Trades: `2,493,179`
- Total Trades Excluding Gifts: `1,139,606` (45.7%)
- Average Bank Per Non Gift Trade: `2.73`
- Total Bank Moved: `3,112,218.81`
- Unique Buyers: `72,061`
- Unique Sellers: `116,020`
- Unique Participants: `126,660`

### 2022:

Comparing these figures with the preceding fiscal year, 2022 showcased a card market with `1,521,153` trades, facilitating a total financial movement of `20,953,130.28` bank.

When excluding gifts, the dataset for 2022 revealed `915,644` trades (or 60.2% of all trades), with an average trade value of `22.88` bank.

Unique buyers in 2022 totaled 62,578, while there were 98,377 sellers, and as a whole 110,398 unique nations participated in cards.

In 2022, there were over `7588` trades that occured with a value of over 250, with `1412` between 250 and 499 and `6177` at over 500.

- Total Trades: `1,521,153`
- Total Trades Excluding Gifts: `915,644` (60.2%)
- Average Bank Per Non Gift Trade: `22.88`
- Total Bank Moved: `20,953,130.28`
- Unique Buyers: `62,578`
- Unique Sellers: `98,377`
- Unique Participants: `110,398`

### Useless Insights

1. It is clear that more trades happened in 2023, but there seems to have been much more player to player or player to puppet interaction in 2023 than in 2022.

2. The changes to market value applied on November of 2022 has had a clear effect on the market. You can see an enormous decline in average trade value from 2022 to 2023, as well as an almost 85.1% decrease in the amount of bank moved via the market. A glance at the amount of trades at a value over 250 tells the same story.

3. Slightly more players participated in cards in 2023, but this could be due to the expansion of puppet armies as much as it could be an increase in unique players.

## More Into 2023 Numbers

The following will be a lot of numbers, a lot of sql queries, and potentially a lot of mistakes.

### 2023 Rarities

The below chart details a breakdown of the movement of rarities on the market during 2023.

| | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
|---|----------|----------|----------| --------- |
| **Common** | 1,237,881 | 555,768 | 1.99 | 1,132,470 |
| **Uncommon** | 517,576 | 244,852 | 1.52 | 373,379 |
| **Rare** | 223,768 | 98,782 | 1.33 | 131,786 |
| **Ultra-Rare** | 193,052 | 92,757 | 1.41 | 130,665 |
| **Epic** | 240,038 | 129,760 | 1.83 | 237,588 |
| **Legendary** | 80,864 | 17,687 | 64 | 1,132,470 |

### 2023 By Season

The below chart details a breakdown of the movement of each season on the market during 2023.

| | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
|---|----------|----------|----------| --------- |
| **S1** | 140,992 | 59,802 | 7.17 | 428,704 |
| **S2** | 330,768 | 146,955 | 7.10 | 1,043,833 |
| **S3** | 2,021,419 | 932,849 | 1.76 | 1,639,682 |

### Season 3 By Both Rarity and Season

The below chart details per season, a breakdown of each card rarity's movement on the market during 2023.

#### Commons

| | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
|---|----------|----------|----------| --------- |
| **S1** | 83,879 | 35,028 | 5.65 | 197,778 |
| **S2** | 211,872 | 97,189 | 6.06 | 589,196 |
| **S3** | 942,220 | 423,551 | 0.76 | 320,469 |

#### Uncommons

| | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
|---|----------|----------|----------| --------- |
| **S1** | 32,279 | 13,645 | 3.55 | 48,413 |
| **S2** | 69,089 | 25,833 | 8.74 | 225,802 |
| **S3** | 416,208 | 205,374 | 0.48 | 98,756 |

#### Rare

| | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
|---|----------|----------|----------| --------- |
| **S1** | 9,473 | 4,027 | 1.49| 5,981 |
| **S2** | 18,747 | 8,298 | 2.35 | 19,501 |
| **S3** | 195,548 | 86,457 | 1.22 | 105,791 |

#### Ultra Rare

| | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
|---|----------|----------|----------| --------- |
| **S1** | 6,132 | 2,713 | 2.85 | 7,738 |
| **S2** | 11,885 | 6,171 | 3.49 | 21,509 |
| **S3** | 175,035 | 83,873 | 1.21 | 101,394 |

#### Epic

| | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
|---|----------|----------|----------| --------- |
| **S1** | 7,286 | 3,834 | 13.68 | 52,460 |
| **S2** | 13,409 | 6,894 | 3.21 | 22,122 |
| **S3** | 219,343 | 119,032 | 1.37 | 162,941 |

#### Legendary

| | Trades Involved In | Non-Gift Trades | Average Price (!0) | Bank Moved |
|---|----------|----------|----------| --------- |
| **S1** | 2,033 | 555 | 210 | 116,334 |
| **S2** | 5,766 | 2,570 | 64.5 | 165,704 |
| **S3** | 73,065 | 14,562 | 58.4 | 850,331 |

## Trades

The below chart details per season, a breakdown of each card rarity's movement on the market during 2023.

### Top Trades of the Year

| Rank | Seller                    | Buyer                      | Price   | Card                                      | Date       |
|------|---------------------------|----------------------------|---------|-------------------------------------------|------------|
| 1    | Ianaterp                   | National Park Service      | 10000.0 | S3 Legendary Annihilators of Chan Island  | 2023-09-04 |
| 2    | new_zander                 | noahs_second_country       | 10000.0 | S3 Legendary Annihilators of Chan Island  | 2023-08-15 |
| 3    | Feu de Glace               | valkyrie_reborn             | 9999.99 | S3 Legendary Annihilators of Chan Island  | 2023-10-01 |
| 4    | 9003                       | 9006                       | 6000.0  | S1 Epic 9003                              | 2023-12-20 |
| 5    |Lilanina                   | osheiga                    | 5000.5  | S3 Legendary Annihilators of Chan Island  | 2023-08-30 |
| 6    | 9003                       | 9006                       | 5000.0  | S2 Common HMS Warmaiden                   | 2023-02-22 |
| 7    | United Worlds of Waifuland | Aerilia                    | 5000.0  | S3 Legendary Annihilators of Chan Island  | 2023-11-02 |
| 8    | Abolished Reality          | Aerilia                    | 4500.0  | S3 Legendary Morover                       | 2023-11-02 |
| 9    | Noahs Second Country       | Fauzjhia                   | 4444.67 | S3 Legendary Morover                       | 2023-04-09 |
| 10   | Midlands                   | 9006                       | 3999.75 | S1 Epic 9003                              | 2023-10-10 |

### Top Common Trades of the Year

| Rank | Seller                   | Buyer                        | Price   | Card                                   | Date       |
|------|--------------------------|------------------------------|---------|----------------------------------------|------------|
| 1    | 9006                     | 9003                         | 5000.0  | S2 Common HMS Warmaiden               | 2023-02-22 |
| 2    | 9006                     | 9003                         | 3000.0  | S2 Common Trytuio                     | 2023-04-17 |
| 3    | 9006                     | 9003                         | 2000.0  | S2 Common Barbaria Trade Federation   | 2023-04-09 |
| 4    | Rastarda                 | Axixic                       | 1000.0  | S1 Common The Britannian Order        | 2023-06-27 |
| 5    | Axixic                   | Rastarda                     | 901.1   | S1 Common The Britannian Order        | 2023-06-27 |
| 6    | Some Random TNP Nation   | Aerilia                      | 750.0   | S2 Common Zazquatch                   | 2023-07-11 |
| 7    | Dorti Saingsmeistan      | Aerilia                      | 750.0   | S2 Common Zazquatch                   | 2023-07-11 |
| 8    | Aerilla                  | Aerilia                      | 750.0   | S2 Common Zazquatch                   | 2023-07-11 |
| 9    | Decen Inn Ash            | Aerilla                      | 705.0   | S2 Common Zazquatch                   | 2023-07-11 |
| 10   | Purple Fairy             | Dorti Saingsmeistan           | 696.0   | S2 Common Zazquatch                   | 2023-07-11 |

### Top Uncommon Trades of the Year

| Rank | Seller   | Buyer   | Price   | Card                   | Date       |
|------|----------|---------|---------|------------------------|------------|
| 1    | Varanius | Vara 3  | 2000.0  | S2 Uncommon Varanius   | 2023-12-09 |
| 2    | Varanius | Vara 1  | 2000.0  | S2 Uncommon Varanius   | 2023-12-09 |
| 3    | Varanius | Vara 2  | 2000.0  | S2 Uncommon Varanius   | 2023-12-09 |
| 4    | Varanius | Vara 5  | 2000.0  | S2 Uncommon Varanius   | 2023-12-09 |
| 5    | Varanius | Vara 4  | 2000.0  | S2 Uncommon Varanius   | 2023-12-09 |
| 6    | Vara 2   | Vara 6  | 1800.02 | S2 Uncommon Varanius   | 2023-12-09 |
| 7    | Vara 3   | Vara 7  | 1800.02 | S2 Uncommon Varanius   | 2023-12-09 |
| 8    | Vara 5   | Vara 9  | 1800.01 | S2 Uncommon Varanius   | 2023-12-09 |
| 9    | Vara 4   | Vara 8  | 1800.01 | S2 Uncommon Varanius   | 2023-12-09 |
| 10   | Vara 1   | Vara 10 | 1800.0  | S2 Uncommon Varanius   | 2023-12-09 |

### Top Rare Trades of the Year

| Rank | Seller             | Buyer             | Price  | Card                         | Date       |
|------|--------------------|-------------------|--------|------------------------------|------------|
| 1    | 9006               | 9003              | 1000.0 | S2 Shin Bet                  | 2023-05-02 |
| 2    | TheLandOfFunFunFun | Upper Tuchoim     | 350.0  | S3 Upper Tuchoim             | 2023-09-13 |
| 3    | Vylixan Dora       | Upper Tuchoim     | 333.33 | S3 Upper Tuchoim             | 2023-12-29 |
| 4    | Calyxion            | Upper Tuchoim     | 333.33 | S3 Upper Tuchoim             | 2023-12-23 |
| 5    | Tropical Isles      | Upper Tuchoim     | 333.33 | S3 Upper Tuchoim             | 2023-12-23 |
| 6    | Volstrostia         | Upper Tuchoim     | 333.33 | S3 Upper Tuchoim             | 2023-12-09 |
| 7    | War Dogs IV         | Upper Tuchoim     | 333.33 | S3 Upper Tuchoim             | 2023-12-06 |
| 8    | Upper Tuchoim       | Bigboy245         | 319.0  | S3 Upper Tuchoim             | 2023-09-16 |
| 9    | Bigboy245           | Bigboy170         | 314.0  | S3 Upper Tuchoim             | 2023-09-16 |
| 10   | Bigboy170           | Bigboy184         | 302.0  | S3 Upper Tuchoim             | 2023-09-15 |

###  Top Ultra Rare Trades of the Year

| Rank | Seller                  | Buyer               | Price  | Card                                 | Date       |
|------|-------------------------|---------------------|--------|--------------------------------------|------------|
| 1    | Upper Tuchoim           | New Kowloon Bay     | 1261.0 | S3 New Kowloon Bay       | 2023-07-10 |
| 2    | Discgolfland            | 90013               | 420.24 | S2 9003                  | 2023-01-14 |
| 3    | ByzKorda                | 9009                | 420.12 | S2 9003                  | 2023-01-14 |
| 4    | Tmasirtup               | New Kowloon Bay     | 399.99 | S1 Improving Wordiness   | 2023-08-26 |
| 5    | Nazten                  | 9001                | 390.0  | S2 9003                  | 2023-04-08 |
| 6    | Mikeswill               | Brexas7             | 273.02 | S1 Brexas                | 2023-10-09 |
| 7    | Koshava                 | Brexas7             | 250.0  | S1 Brexas                | 2023-12-18 |
| 8    | Portsville              | Brexas7             | 200.05 | S1 Brexas                | 2023-05-22 |
| 9    | Varanius                | Brexas7             | 200.03 | S1 Brexas2               | 2023-10-28 |
| 10   | TheLandOfFunFunFun      | The Funian Conduit  | 160.2  | S3 TheLandOfFunFunFun     | 2023-03-28 |

### Top Epic Trades of the Year

| Rank | Seller          | Buyer           | Price  | Card        | Date       |
|------|-----------------|------------------|--------|-------------|------------|
| 1    | 9003            | 9006            | 6000.0 | S1 9003 | 2023-12-20 |
| 2    | Midlands         | 9006            | 3999.75| S1 9003 | 2023-10-10 |
| 3    | Osheiga          | 9006            | 2000.0 | S1 9003 | 2023-07-28 |
| 4    | Timao            | 9006            | 2000.0 | S1 9003 | 2023-07-28 |
| 5    | 900100           | 9006            | 1110.0 | S1 9003 | 2023-08-20 |
| 6    | 900101           | 9006            | 1099.29| S1 9003 | 2023-08-20 |
| 7    | 900103           | Federationalism | 1000.5 | S1 9003 | 2023-08-20 |
| 8    | 900104           | 900100          | 1000.0 | S1 9003 | 2023-08-20 |
| 9    | 900102           | 900101          | 1000.0 | S1 9003 | 2023-08-20 |
| 10   | 9003            | 9006            | 1000.0 | S1 9003 | 2023-05-23 |

### Top Legendary Trades of the Year

| Rank | Seller                   | Buyer                     | Price   | Card                                     | Date       |
|------|--------------------------|---------------------------|---------|------------------------------------------|------------|
| 1    | Ianaterp                  | National Park Service     | 10000.0 | S3 Annihilators of Chan Island | 2023-09-04 |
| 2    | New Zander                | Noahs Second Country      | 10000.0 | S3 Annihilators of Chan Island | 2023-08-15 |
| 3    | Feu De Glace              | Valkyrie Reborn            | 9999.99 | S3 Annihilators of Chan Island | 2023-10-01 |
| 4    | Lilanina                  | Osheiga                   | 5000.5  | S3 Annihilators of Chan Island | 2023-08-30 |
| 5    | United Worlds of Waifuland| Aerilia                   | 5000.0  | S3 Annihilators of Chan Island | 2023-11-02 |
| 6    | Abolished Reality         | Aerilia                   | 4500.0  | S3 Morover                      | 2023-11-02 |
| 7    | Noahs Second Country      | Fauzjhia                  | 4444.67 | S3 Morover                      | 2023-04-09 |
| 8    | Tupan                     | National Park Service     | 2000.0  | S3 Chan Island                  | 2023-08-17 |
| 9    | 9006                      | Siwale                    | 2000.0  | S3 Morover                      | 2023-12-26 |
| 10   | Aerilia                   | Aragesh                   | 1600.0  | S1 Soops                        | 2023-08-20 |

### Top S1 Legendary Trades of the Year

| Rank | Seller                 | Buyer                  | Price   | Card                  | Date       |
|------|------------------------|------------------------|---------|-----------------------|------------|
| 1    | Aerilia                | Aragesh                | 1600.0  | S1 Soops    | 2023-08-20 |
| 2    | Alcala Cordel          | The First Galactic Republic | 1000.0  | S1 Testlandia | 2023-04-09 |
| 3    | Refuge Isle            | Tape                   | 900.0   | S1 Testlandia | 2023-10-30 |
| 4    | Racoda                 | Numero Capitan         | 862.22  | S1 Foucaults Garden | 2023-07-24 |
| 5    | Izern                  | Federationalism        | 800.0   | S1 Testlandia | 2023-06-23 |
| 6    | Refuge Isle            | Portsville             | 755.0   | S1 Testlandia | 2023-11-29 |
| 7    | Refuge Isle            | Succedania             | 750.01  | S1 Testlandia | 2023-12-02 |
| 8    | Portsville             | Osheiga                | 750.0   | S1 Rubyna   | 2023-07-30 |
| 9    | Elegarth               | War Dogs IV            | 750.0   | S1 Rubyna   | 2023-11-10 |
| 10   | Racoda                 | New Kowloon Bay        | 738.89  | S1 NERVUN   | 2023-08-25 |

### Individual Cards

#### Most Moved Cards

| Rank | Card | Trade Count |
| - | ---- | ----------- |
| 1 | S2 Common El Alto Parana | 16,125
| 2 |  S2 -ii |12,366 |
| 3 | S2 Pittsburgh Penguins | 12,197 |
| 4 | S2 Common Southern Defender 26 | 6,779 |
| 5 | S2 Common Northern Lands Islannibady | 4,821 |
| 6 | S1 Common Rahmaostan | 4,654 |
| 7 | S3 Uncommon Yuantoplae lesplay | 4,294 |
| 8 | S3 Uncommon Smeagollum | 4,153 |
| 9 | S3 Common Chitose Ikeda | 4,095 |
| 10 | S3 Rare Valoptia | 4,040 |

#### Most Bank Moved Per Card

| Rank | Card                              | Money Moved        | Transfer Count |
|------|-----------------------------------|--------------------|-----------------|
| 1    | S2 Common Pittsburgh Penguins    | 59,193.26          | 12,197          |
| 2    | S2 Common -ii                    | 56,284.65          | 12,366          |
| 3    | S2 Uncommon Varanius             | 40,608.31          | 130             |
| 4    | S3 Legendary Annihilators of Chan Island | 40,000.49  | 28              |
| 5    | S2 Common El Alto Parana          | 32,309.72          | 16,125          |
| 6    | S1 Epic 9003                      | 27,392.05          | 45              |
| 7    | S2 Uncommon Panagouge             | 24,286.70          | 119             |
| 8    | S3 Rare Upper Tuchoim             | 23,804.57          | 529             |
| 9    | S3 Legendary The Stalker          | 21,509.52          | 471             |
| 10   | S2 Common Sacara                  | 20,563.57          | 156             |

### Most Traded Legendary

| Rank | Card Name               | Trades |
|------|-------------------------|--------|
| 1    | S3 The Stalker          | 126    |
| 2    | S3 Valkalan             | 117    |
| 3    | S3 Koem Kab             | 97     |
| 4    | S3 Australian rePublic  | 89     |
| 5    | S3 Xagill               | 89     |
| 6    | S3 Wrapper              | 87     |
| 7    | S3 Felpolandia          | 86     |
| 8    | S3 Siwale               | 85     |
| 9    | S3 Corfad               | 83     |
| 10   | S3 Lamoni               | 83     |

#### Most Bank Moved By Legendary

| Rank | Card Name                     | Money Moved |
|------|-------------------------------|-------------|
| 3    | S3 Annihilators of Chan Island | 40000.49    |
| 3    | S3 The Stalker                | 21509.52    |
| 2    | S2 Sacara                     | 20563.57    |
| 3    | S3 Racoda                     | 17975.14    |
| 3    | S3 Crazy girl                 | 17869.38    |
| 3    | S3 Sedgistan                  | 16638.13    |
| 3    | S3 Giovanniland               | 16051.36    |
| 3    | S3 Noahs Second Country        | 15533.62    |
| 2    | S2 S_diego                    | 15372.87    |
| 3    | S3 Morover                    | 14054.69    |

## Buyers and Sellers

This next section will focus on the players of the game: those that bought and sold cards.

### Bank Movers

#### Most Bank Moved

| Rank | Trader               | Total Money Moved  |
|------|----------------------|--------------------|
| 1    | Noahs Second Country | 223207.0           |
| 2    | Mikeswill            | 187134.69          |
| 3    | Koem Kab             | 175546.73          |
| 4    | Osheiga              | 131383.33          |
| 5    | Seanat               | 112887.81          |
| 6    | Varanius             | 103207.39          |
| 7    | Giovanniland         | 82404.1            |
| 8    | Fauzjhia             | 78895.19           |
| 9    | 9006                 | 78616.81           |
| 10   | Vulxo                | 67605.57           |

#### Bank Moved as buyer

| Rank | Trader                   | Money Moved           |
|------|--------------------------|-----------------------|
| 1    | Noahs Second Country     | 90,030.04             |
| 2    | Koem Kab                 | 84,596.00             |
| 3    | Mikeswill                | 76,428.20             |
| 4    | Osheiga                  | 62,617.93             |
| 5    | Seanat                   | 54,837.61             |
| 6    | Varanius                 | 48,412.59             |
| 7    | Giovanniland             | 38,408.73             |
| 8    | 9006                     | 36,446.13             |
| 9    | Fauzjhia                 | 34,779.57             |
| 10   | Portsville               | 33,509.21             |

#### Bank Moved as seller

| Rank | Trader               | Money_Moved           |
|------|----------------------|-----------------------|
| 1    | Noahs Second_Country | 141036.96             |
| 2    | Mikeswill             | 120877.49             |
| 3    | Koem Kab              | 91041.49              |
| 4    | Osheiga               | 69225.65              |
| 5    | Seanat               | 58050.20              |
| 6    | Varanius              | 57205.29              |
| 7    | Fauzjhia              | 46342.89              |
| 8    | Giovanniland          | 44005.59              |
| 9    | 9006                 | 43668.90              |
| 10   | Thorn1000             | 39490.27              |

### Trade Count

#### Most Active Traders

| Rank | Trader                  | Trade Count |
|------|-------------------------|-------------|
| 1    | War Dogs IV             | 314,455     |
| 2    | The Colonial Buccaruu   | 102,381     |
| 3    | Dune Cat                | 50,428      |
| 4    | Mikeswill               | 41,448      |
| 5    | Noahs Second Country    | 37,603      |
| 6    | Giovanniland            | 36,643      |
| 7    | Koem Kab                | 34,226      |
| 8    | Fauzjhia                | 31,934      |
| 9    | New Makasta             | 31,816      |
| 10   | Apexiala                | 27,283      |

#### Most Active Traders Non-Zero

| Rank | Trader                                     | Trade Count |
|------|--------------------------------------------|-------------|
| 1    | War Dogs IV                                | 46,409      |
| 2    | Dune Cat                                   | 39,037      |
| 3    | Giovanniland                               | 27,060      |
| 4    | Il Sonno della Ragione Genera Mostri       | 25,438      |
| 5    | Apexiala                                    | 20,609      |
| 6    | Frisbeeteria                               | 19,334      |
| 7    | New Makasta                                | 17,405      |
| 8    | Noah's Second Country                      | 14,810      |
| 9    | Giraffeton                                 | 14,794      |
| 10   | Krupp Industries                           | 13,873      |

#### Most Cards Bought

| Rank | Trader                                  | Cards Bought |
|------|-----------------------------------------|-------------------|
| 1    | War Dogs IV                             | 265,591           |
| 2    | The Colonial Buccaruu                   | 95,280            |
| 3    | Dune Cat                                | 48,965            |
| 4    | Giovanniland                            | 34,072            |
| 5    | Mikeswill                               | 28,802            |
| 6    | Koem Kab                                | 25,351            |
| 7    | Apexiala                                | 23,973            |
| 8    | New Makasta                             | 23,435            |
| 9    | Noah's Second Country                   | 22,626            |
| 10   | Il Sonno della Ragione Genera Mostri    | 18,821            |


#### Most Cards Bought For More Than Zero

| Rank | Trader                                  | Total Money Moved |
|------|-----------------------------------------|-------------------|
| 1    | Dune Cat                                | 37,590            |
| 2    | Giovanniland                            | 25,288            |
| 3    | War Dogs IV                             | 22,028            |
| 4    | Apexiala                                | 19,055            |
| 5    | Il Sonno della Ragione Genera Mostri    | 18,783            |
| 6    | Frisbeeteria                            | 15,545            |
| 7    | Giraffeton                              | 13,693            |
| 8    | The North Pacific S3                    | 12,077            |
| 9    | Sentient Puppets                        | 10,420            |
| 10   | Rain Delay                              | 9,682             |


#### Most Cards Sold

| Rank | Trader                                | Total Money Moved |
|------|---------------------------------------|-------------------|
| 1    | War Dogs IV                           | 48,864            |
| 2    | Noah's Second Country                 | 14,977            |
| 3    | Fauzjhia                              | 14,462            |
| 4    | Mikeswill                             | 12,646            |
| 5    | A Share of the JPMorgan Chase         | 11,617            |
| 6    | Seanat                                | 9,962             |
| 7    | Koem Kab                              | 8,875             |
| 8    | Axixic                                | 8,659             |
| 9    | New Makasta                           | 8,381             |
| 10   | Thorn1000                             | 7,195             |


#### Most Cards Sold For More Than Zero

| Rank | Trader                                  | Trade Count |
|------|-----------------------------------------|-------------|
| 1    | War Dogs IV                             | 24,381      |
| 2    | Noah's Second Country                   | 12,817      |
| 3    | Koem Kab                                | 8,869       |
| 4    | Axixic                                  | 8,358       |
| 5    | New Makasta                             | 8,281       |
| 6    | Mikeswill                               | 7,471       |
| 7    | Il Sonno della Ragione Genera Mostri    | 6,655       |
| 8    | Thorn1000                               | 5,848       |
| 9    | Seanat                                  | 5,692       |
| 10   | Fauzjhia                                | 5,653       |

#### Most Cards Gifted

| Rank | Trader                                | Trade Count |
|------|---------------------------------------|-------------|
| 1    | War Dogs IV                           | 24,483      |
| 2    | Fauzjhia                              | 8,809       |
| 3    | A Share of the JPMorgan Chase         | 6,600       |
| 4    | Mikeswill                             | 5,175       |
| 5    | Seanat                                | 4,270       |
| 6    | Demeter                               | 3,986       |
| 7    | Yodle                                 | 3,624       |
| 8    | The Colonial Buccaruu                 | 2,566       |
| 9    | Aerilia                               | 2,351       |
| 10   | Noah's Second Country                 | 2,160       |


#### Most Cards Bought (250+)

| Rank | Trader            | Cards Bought |
|------|-------------------|-----------------|
| 1    | Osheiga           | 69              |
| 2    | Giovanniland      | 69              |
| 3    | Fauzjhia          | 36              |
| 4    | Upper Tuchoim     | 31              |
| 5    | Vulxo             | 24              |
| 6    | Varanius          | 23              |
| 7    | Seanat            | 23              |
| 8    | Valoptia          | 21              |
| 9    | Pumpty Dumpty     | 19              |
| 10   | Portsville        | 17              |

#### Most Cards Sold (250+)

| Rank | Trader          | Transfer Count |
|------|-----------------|-----------------|
| 1    | Giovanniland    | 47              |
| 2    | Varanius        | 25              |
| 3    | Osheiga         | 19              |
| 4    | Racoda          | 17              |
| 5    | Panagouge       | 17              |
| 6    | Vulxo           | 16              |
| 7    | 9006            | 16              |
| 8    | Benevolent 1    | 15              |
| 9    | Fauzjhia        | 11              |
| 10   | Dr Hooves       | 10              |

### Buyers By Season


#### Season 1

| Rank | Trader           | Cards Bought |
|------|------------------|-------------|
| 1    | Cartagriem 011   | 4,291       |
| 2    | Kwaj             | 3,793       |
| 3    | Mikeswill         | 3,584       |
| 4    | Koem Kab         | 3,008       |
| 5    | Rain Delay       | 2,948       |
| 6    | War Dogs IV      | 2,848       |
| 7    | Ballotonia       | 2,657       |
| 8    | Kractero          | 2,622       |
| 9    | War Dogs VII     | 2,605       |
| 10   | Talakmachen      | 2,276       |

#### Season 1 Non-Zero

| Rank | Trader                     | Cards Bought |
|------|----------------------------|-------------|
| 1    | Cartagriem_011             | 2,321       |
| 2    | War Dogs IV                | 2,144       |
| 3    | Rain Delay                 | 1,636       |
| 4    | Mikeswill                  | 1,515       |
| 5    | Caffeinated                | 1,221       |
| 6    | Dr_Hooves                  | 856         |
| 7    | Yodle                      | 767         |
| 8    | Apexiala                   | 722         |
| 9    | Ferengi Alliance Union     | 682         |
| 10   | Mikeshope                  | 624         |

#### Season 2

| Rank | Trader                            | Money Moved |
|------|-----------------------------------|-------------|
| 1    | Mikeswill                          | 17,792      |
| 2    | Noahs Second Country               | 14,215      |
| 3    | Koem Kab                           | 10,639      |
| 4    | New Makasta                        | 9,812       |
| 5    | Seanat                             | 7,142       |
| 6    | Witchcraft and Sorcery             | 5,255       |
| 7    | A Share of the JPMorgan Chase      | 3,307       |
| 8    | Giovanniland                       | 3,182       |
| 9    | Annondor                            | 2,853       |
| 10   | Rain Delay                          | 2,831       |

#### Season 2 Non-Zero

| Rank | Trader                              | Cards Bought |
|------|-------------------------------------|-------------|
| 1    | Annondor                            | 2,851       |
| 2    | Rain Delay                          | 1,947       |
| 3    | Ballo                               | 1,740       |
| 4    | Il Sonno della Ragione Genera Mostri| 1,594       |
| 5    | 9006                                | 1,542       |
| 6    | Mikeswill                           | 1,491       |
| 7    | Ferengi Alliance Union               | 1,054       |
| 8    | Krupp Industries                    | 965         |
| 9    | Apexiala                             | 910         |
| 10   | Seanat                              | 890         |

#### Season 3

>Buyer of Season 3:

| Rank | Trader                     | Cards Bought |
|------|----------------------------|-------------|
| 1    | War Dogs IV                | 261,276     |
| 2    | The Colonial Buccaruu      | 93,698      |
| 3    | Dune Cat                   | 47,995      |
| 4    | Giovanniland               | 30,277      |
| 5    | Apexiala                    | 20,429      |
| 6    | Giraffeton                  | 18,722      |
| 7    | Il Sonno della Ragione Genera Mostri | 16,729 |
| 8    | Fastercat                   | 16,710      |
| 9    | Racoda                     | 16,226      |
| 10   | Fauzjhia                    | 15,568      |

#### Season 3 Non-Zero

| Rank | Trader                              | Cards Bought |
|------|-------------------------------------|-------------|
| 1    | Dune Cat                            | 37,589      |
| 2    | Giovanniland                        | 24,938      |
| 3    | War Dogs IV                         | 19,698      |
| 4    | Apexiala                             | 17,423      |
| 5    | Il Sonno della Ragione Genera Mostri| 16,692      |
| 6    | Frisbeeteria                        | 15,316      |
| 7    | Giraffeton                           | 13,630      |
| 8    | The North Pacific S3                | 12,075      |
| 9    | Sentient Puppets                     | 10,417      |
| 10   | New Makasta                          | 9,020       |

### Buyers By Rarity Non-Zero

#### Common

| Rank | Trader                              | Cards Bought |
|------|-------------------------------------|-------------|
| 1    | Giovanniland                        | 21,954      |
| 2    | War Dogs IV                         | 18,071      |
| 3    | Il Sonno della Ragione Genera Mostri| 15,848      |
| 4    | Apexiala                             | 15,008      |
| 5    | Giraffeton                           | 11,506      |
| 6    | The North Pacific S3                | 9,231       |
| 7    | Sentient Puppets                     | 6,016       |
| 8    | Witchcraft and Sorcery               | 5,195       |
| 9    | Concrete Slab                       | 4,900       |
| 10   | Krupp Industries                    | 4,729       |

#### Uncommon

| Rank | Trader                    | Cards Bought |
|------|---------------------------|--------------|
| 1    | Dune Cat                  | 37,578       |
| 2    | Racoda                    | 5,202        |
| 3    | S3 Rares Collector        | 4,049        |
| 4    | Altivia Central Bank      | 3,369        |
| 5    | War Dogs IV               | 2,941        |
| 6    | Annondor                  | 2,705        |
| 7    | Pierpontia                | 2,700        |
| 8    | Rain Delay                | 2,563        |
| 9    | Apexiala                   | 2,485        |
| 10   | Giovanniland              | 2,372        |

#### Rare

| Rank | Trader                 | Cards Bought |
|------|------------------------|--------------|
| 1    | New Zander             | 7,635        |
| 2    | S3 Rares Collector     | 2,185        |
| 3    | Sentient Puppets       | 2,008        |
| 4    | Annondor               | 1,797        |
| 5    | Midlands               | 1,392        |
| 6    | Pierpontia             | 1,296        |
| 7    | Demeter                | 1,210        |
| 8    | Rain Delay             | 1,051        |
| 9    | Slaggstone Bruntt      | 886          |
| 10   | Krupp Industries       | 846          |

#### Ultra Rare

| Rank | Trader             | Cards Bought |
|------|--------------------|--------------|
| 1    | Radicalania        | 6,501        |
| 2    | Ostrovskiy         | 6,447        |
| 3    | Midlands           | 2,340        |
| 4    | Demeter            | 1,662        |
| 5    | Rain Delay         | 1,156        |
| 6    | Mikeswill          | 1,140        |
| 7    | Fauzjhia           | 776          |
| 8    | Timao              | 740          |
| 9    | Giraffeton         | 684          |
| 10   | Slaggstone Bruntt  | 662          |

#### Epic

| Rank | Trader                     | Cards Bought |
|------|----------------------------|--------------|
| 1    | Frisbeeteria               | 15,534       |
| 2    | Fauzjhia                   | 3,873        |
| 3    | Tuptoogza                  | 2,067        |
| 4    | Midlands                   | 2,052        |
| 5    | Altivia Stock Exchange     | 1,850        |
| 6    | Celzlhi                    | 1,780        |
| 7    | Timao                      | 1,749        |
| 8    | Discgolfland               | 1,641        |
| 9    | Shion Uzuki                | 1,582        |
| 10   | Auranzjinilhe               | 1,350       |

### Legendaries

#### Legendaries Bought

| Rank | Trader                                | Trade Count |
|------|---------------------------------------|-------------|
| 1    | Koem Kab                              | 8,604       |
| 2    | Noah's Second Country                 | 7,789       |
| 3    | Mikeswill                             | 4,508       |
| 4    | Seanat                                | 2,150       |
| 5    | Thorn1000                             | 1,833       |
| 6    | New Makasta                           | 1,803       |
| 7    | Portsville                            | 1,567       |
| 8    | National Park Service                 | 1,539       |
| 9    | Varanius                              | 1,479       |
| 10   | Osheiga                               | 1,399       |

#### Legendaries Bought Non-Zero

| Rank | Trader                                | Trade Count |
|------|---------------------------------------|-------------|
| 1    | Koem Kab                              | 2,272       |
| 2    | Noah's Second Country                 | 1,232       |
| 3    | Mikeswill                             | 1,004       |
| 4    | Seanat                                | 815         |
| 5    | Portsville                            | 695         |
| 6    | Thorn1000                             | 452         |
| 7    | New Makasta                           | 451         |
| 8    | Osheiga                               | 326         |
| 9    | The Shaymen                           | 293         |
| 10   | Vulxo                                 | 291         |

#### Legendaries Gifted

| Rank | Trader                        | Trade Count |
|------|-------------------------------|-------------|
| 1    | Seanat                        | 436         |
| 2    | Valoptia                      | 415         |
| 3    | Lackadaisia                   | 384         |
| 4    | The Chinese Soviet            | 374         |
| 5    | 9006                          | 314         |
| 6    | Refuge Isle                   | 274         |
| 7    | ROM                           | 270         |
| 8    | Thorn1000                     | 259         |
| 9    | The Northern Light            | 251         |
| 10   | Greatest Chernobyl            | 223         |

#### Legendaries Received

| Rank | Trader                      | Trade Count |
|------|-----------------------------|-------------|
| 1    | Noah's Second Country       | 6,557       |
| 2    | Koem Kab                    | 6,332       |
| 3    | Mikeswill                   | 3,504       |
| 4    | National Park Service       | 1,471       |
| 5    | Thorn1000                   | 1,381       |
| 6    | New Makasta                 | 1,352       |
| 7    | Seanat                      | 1,335       |
| 8    | Varanius                    | 1,278       |
| 9    | Osheiga                     | 1,073       |
| 10   | Valoptia                    | 917         |

## Time Breakdown

### First Half of the Year

#### Most Bank Moved

| Rank | Trader                   | Money Moved           |
|------|--------------------------|-----------------------|
| 1    | Noah's Second Country    | 135773.33             |
| 2    | Mikeswill                | 88768.78              |
| 3    | Seanat                   | 59438.93              |
| 4    | Koem Kab                 | 51452.39              |
| 5    | Osheiga                  | 46866.87              |
| 6    | 9006                     | 42751.25              |
| 7    | Fauzjhia                 | 41227.25              |
| 8    | Portsville               | 37797.21              |
| 9    | Giraffeton               | 34535.02              |
| 10   | Thorn1000                | 32512.42              |

#### Most Bank Moved as Buyer

| Rank | Trader               | Money_Moved           |
|------|----------------------|-----------------------|
| 1    | Noahs Second Country | 59924.76              |
| 2    | Mikeswill             | 42387.20              |
| 3    | Seanat               | 26402.06              |
| 4    | 9006                 | 19667.27              |
| 5    | Koem Kab              | 19217.22              |
| 6    | Portsville            | 18240.34              |
| 7    | Fauzjhia              | 17731.29              |
| 8    | Osheiga               | 17543.93              |
| 9    | Varanius              | 16332.42              |
| 10   | Thorn1000             | 15578.46              |

#### Most Bank Moved as Seller

| Rank | Trader               | Money_Moved           |
|------|----------------------|-----------------------|
| 1    | Noahs Second Country | 75848.57              |
| 2    | Mikeswill             | 46381.58              |
| 3    | Seanat               | 33036.87              |
| 4    | Koem_Kab              | 32235.17              |
| 5    | Osheiga               | 29322.94              |
| 6    | Giraffeton            | 24813.47              |
| 7    | Fauzjhia              | 23495.96              |
| 8    | 9006                 | 23083.98              |
| 9    | Portsville            | 19556.87              |
| 10   | New Makasta           | 17329.53              |

#### Most Cards Bought

| Rank | Trader                  | Cards Bought |
|------|-------------------------|--------------|
| 1    | War Dogs IV             | 100449       |
| 2    | Dune Cat                | 48862        |
| 3    | The Colonial Buccaruu   | 42122        |
| 4    | Racoda                  | 17158        |
| 5    | Giovanniland            | 16970        |
| 6    | Mikeswill               | 16651        |
| 7    | Apexiala                | 14368        |
| 8    | The North Pacific S3    | 13450        |
| 9    | Noahs Second Country    | 13347        |
| 10   | Slaggstone Bruntt       | 12829        |

#### Most Cards Bought Non-Zero

| Rank | Trader                             | Cards Bought |
|------|------------------------------------|--------------|
| 1    | Dune Cat                            | 37510        |
| 2    | War Dogs IV                         | 14138        |
| 3    | The North Pacific S3                | 12071        |
| 4    | Giovanniland                        | 11713        |
| 5    | Apexiala                             | 11399        |
| 6    | Il Sonno Della Ragione Genera Mostri | 10028        |
| 7    | Frisbeeteria                        | 8810         |
| 8    | Annondor                            | 8721         |
| 9    | S3 Rares Collector                  | 6947         |
| 10   | Giraffeton                          | 6532         |

#### Most Cards Sold

| Rank | Trader                             | Cards Bought |
|------|------------------------------------|--------------|
| 1    | War Dogs IV                         | 24218        |
| 2    | Noahs Second Country                | 9214         |
| 3    | Mikeswill                           | 7634         |
| 4    | A Share of the JPMorgan Chase       | 6067         |
| 5    | Seanat                              | 5627         |
| 6    | Axixic                              | 4915         |
| 7    | Fauzjhia                            | 4746         |
| 8    | New Makasta                         | 4381         |
| 9    | Witchcraft and Sorcery              | 3685         |
| 10   | Il Sonno Della Ragione Genera Mostri | 3152        |

#### Most Cards Sold Non-Zero

| Rank | Trader                             | Cards Bought |
|------|------------------------------------|--------------|
| 1    | War Dogs IV                         | 8697         |
| 2    | Noahs Second Country                | 7067         |
| 3    | Axixic                              | 4750         |
| 4    | New Makasta                         | 4318         |
| 5    | Mikeswill                           | 4037         |
| 6    | Seanat                              | 3728         |
| 7    | Witchcraft and Sorcery              | 3421         |
| 8    | Il Sonno Della Ragione Genera Mostri | 3152        |
| 9    | Koem Kab                            | 3079         |
| 10   | Krupp Industries                    | 2762         |

### Last Half of the Year

#### Most Bank Moved

| Rank | Trader                   | Money Moved           |
|------|--------------------------|-----------------------|
| 1    | Koem Kab                 | 124094.34             |
| 2    | Mikeswill                | 98365.91              |
| 3    | Noah's Second Country    | 87433.67              |
| 4    | Osheiga                  | 84516.46              |
| 5    | Varanius                 | 71317.45              |
| 6    | Giovanniland             | 53957.49              |
| 7    | Upper Tuchoim            | 53916.52              |
| 8    | Seanat                   | 53448.88              |
| 9    | Vulxo                    | 52174.08              |
| 10   | Panagouge                | 41919.98              |

#### Most Bank Moved as Buyer

| Rank | Trader                   | Money Moved           |
|------|--------------------------|-----------------------|
| 1    | Koem Kab                 | 65378.78              |
| 2    | Osheiga                  | 45074.00              |
| 3    | Mikeswill                | 34041.00              |
| 4    | Varanius                 | 32080.17              |
| 5    | Noah's Second Country    | 30105.28              |
| 6    | Seanat                   | 28435.55              |
| 7    | Vulxo                    | 25479.53              |
| 8    | Upper Tuchoim            | 25266.64              |
| 9    | Giovanniland             | 23139.56              |
| 10   | Aerilia                  | 22435.47              |

#### Most Bank Moved as Seller

| Rank | Trader                   | Money Moved           |
|------|--------------------------|-----------------------|
| 1    | Mikeswill                | 64324.91              |
| 2    | Koem Kab                 | 58715.56              |
| 3    | Noah's Second Country    | 57328.39              |
| 4    | Osheiga                  | 39442.46              |
| 5    | Varanius                 | 39237.28              |
| 6    | Giovanniland             | 30817.93              |
| 7    | Upper Tuchoim            | 28649.88              |
| 8    | Vulxo                    | 26694.55              |
| 9    | Panagouge                 | 25716.52              |
| 10   | Seanat                   | 25013.33              |

#### Most Cards Bought

| Rank | Trader                   | Cards Bought |
|------|--------------------------|--------------|
| 1    | War Dogs IV              | 165142       |
| 2    | The Colonial Buccaruu    | 53158        |
| 3    | Koem Kab                 | 18556        |
| 4    | Giovanniland             | 17102        |
| 5    | Mikeswill                | 12151        |
| 6    | Fauzjhia                 | 11742        |
| 7    | New Makasta              | 10799        |
| 8    | War Dogs VI              | 10272        |
| 9    | Apexiala                 | 9605         |
| 10   | Noah's Second Country    | 9279         |

#### Most Cards Bought Non-Zero

| Rank | Trader                             | Cards Bought |
|------|------------------------------------|--------------|
| 1    | Giovanniland                       | 13575        |
| 2    | Il Sonno della Ragione Genera Mostri| 8755         |
| 3    | New Zander                          | 8044         |
| 4    | War Dogs IV                         | 7890         |
| 5    | Apexiala                             | 7656         |
| 6    | Giraffeton                           | 7161         |
| 7    | Frisbeeteria                         | 6735         |
| 8    | Midlands                             | 5220         |
| 9    | Sentient Puppets                     | 5137         |
| 10   | Rain Delay                           | 5004         |

#### Most Cards Sold

| Rank | Trader                             | Cards Bought |
|------|------------------------------------|--------------|
| 1    | War Dogs IV                         | 24646        |
| 2    | Fauzjhia                            | 9716         |
| 3    | Koem Kab                            | 5793         |
| 4    | Noahs Second Country                | 5763         |
| 5    | A Share of the JPMorgan Chase       | 5550         |
| 6    | Mikeswill                           | 5012         |
| 7    | Thorn1000                           | 4620         |
| 8    | Seanat                              | 4335         |
| 9    | The Colonial Buccaruu               | 4095         |
| 10   | New Makasta                         | 4000         |

#### Most Cards Sold Non-Zero

| Rank | Trader                             | Cards Bought |
|------|------------------------------------|--------------|
| 1    | War Dogs IV                         | 15684        |
| 2    | Koem Kab                            | 5790         |
| 3    | Noahs Second Country                | 5750         |
| 4    | New Makasta                         | 3963         |
| 5    | Thorn1000                           | 3739         |
| 6    | Axixic                              | 3608         |
| 7    | Il Sonno della Ragione Genera Mostri| 3503         |
| 8    | Mikeswill                           | 3434         |
| 9    | Fauzjhia                            | 2943         |
| 10   | Krupp Industries                    | 2770         |

### Hours, Days, Months

#### Most Active Day

The day in which the most money was transferred on the market was December 9th at 7 AM UTC, which totaled 13994.06.

These were the top 5 trades on that day.

| Rank | Seller      | Buyer      | Price   | Card                     |
|------|-------------|------------|---------|--------------------------|
| 1    | Vara 6       | Vara 2     | 1800.02 | S2 Uncommon Varanius    |
| 2    | Vara 7       | Vara 3     | 1800.02 | S2 Uncommon Varanius    |
| 3    | Vara 9       | Vara 5     | 1800.01 | S2 Uncommon Varanius    |
| 4    | Vara 8       | Vara 4     | 1800.01 | S2 Uncommon Varanius    |
| 5    | Vara 10      | Vara 1     | 1800.0  | S2 Uncommon Varanius    |

The day in which the most trades occured on the market was Jan 26th at 10 pm utc, a total of 2060.

The most active buyer at the time was The North Pacific S3, at 1011. Conversely, the most active seller was Amphibian Manifesto, at 49.

#### Hour of the Day

Note: UTC

![Hours of the Day](Hourly.png)

| Hour | Total Trades | Money Moved |
|------|--------------|-------------|
| 00   | 113436       | 149892.53   |
| 01   | 114036       | 155002.44   |
| 02   | 111010       | 144957.68   |
| 03   | 107194       | 148705.67   |
| 04   | 94599        | 136951.67   |
| 05   | 86013        | 130416.53   |
| 06   | 87508        | 125992.13   |
| 07   | 89604        | 139170.92   |
| 08   | 95962        | 199056.45   |
| 09   | 79598        | 120374.23   |
| 10   | 71939        | 83971.04    |
| 11   | 79068        | 75039.10    |
| 12   | 83346        | 75831.76    |
| 13   | 91905        | 93038.80    |
| 14   | 98919        | 101369.13   |
| 15   | 109234       | 103668.68   |
| 16   | 116086       | 127366.42   |
| 17   | 116305       | 138870.67   |
| 18   | 120828       | 133231.79   |
| 19   | 127516       | 143125.11   |
| 20   | 128689       | 147428.60   |
| 21   | 129783       | 146909.10   |
| 22   | 123905       | 157420.83   |
| 23   | 116696       | 134427.53   |

#### Day of the Week

![Days of the Week](Daily.png)

| Day       | Total Trades | Money Moved           |
|-----------|--------------|-----------------------|
| Sunday    | 397266       | 509982.40             |
| Monday    | 352726       | 461864.41             |
| Tuesday   | 352134       | 456240.22             |
| Wednesday | 349130       | 431593.36             |
| Thursday  | 329902       | 411712.97             |
| Friday    | 341741       | 396818.95             |
| Saturday  | 370280       | 444006.50             |

#### Hour vs Day Heatmaps

![Bank Moved heatmap by day and hour](Heatmap.png)
![Trade count heatmap by day and hour](Heatmap2.png)

#### Month of the Year

![Months of the Year](Monthly.png)

| Month    | Total Trades | Money Moved          |
|----------|--------------|----------------------|
| 2023-01  | 271404       | 292793.48            |
| 2023-02  | 193665       | 193129.92            |
| 2023-03  | 222917       | 259635.81            |
| 2023-04  | 185720       | 253606.95            |
| 2023-05  | 219461       | 232034.37            |
| 2023-06  | 185709       | 172846.79            |
| 2023-07  | 209809       | 291856.94            |
| 2023-08  | 231064       | 381505.07            |
| 2023-09  | 188742       | 224038.00            |
| 2023-10  | 185537       | 260495.24            |
| 2023-11  | 195958       | 217322.43            |
| 2023-12  | 203193       | 332953.81            |

### Cards, Traders

#### Traders Per Month Non-Zero

| Year-Month | Trader                | Total Trades |
|------------|-----------------------|--------------|
| 2023-01    | The North Pacific S3  | 10466        |
| 2023-02    | Dune Cat               | 11280        |
| 2023-03    | Dune Cat               | 19287        |
| 2023-04    | Apexiala               | 2713         |
| 2023-05    | War Dogs IV            | 9546         |
| 2023-06    | War Dogs IV            | 4507         |
| 2023-07    | Koem Kab               | 3847         |
| 2023-08    | Giovanniland           | 3003         |
| 2023-09    | War Dogs IV            | 2697         |
| 2023-10    | Noah's Second Country  | 3528         |
| 2023-11    | New Zander             | 6890         |
| 2023-12    | War Dogs IV            | 3003         |

#### Most Bank Moved Per Month

| Year-Month | Trader                | Money Moved |
|------------|-----------------------|-------------|
| 2023-01    | Noah's Second Country | 19633.92    |
| 2023-02    | Giraffeton            | 12164.69    |
| 2023-03    | Noah's Second Country | 19653.21    |
| 2023-04    | Noah's Second Country | 21982.61    |
| 2023-05    | Seanat                | 11530.6     |
| 2023-06    | Koem Kab              | 8970.3      |
| 2023-07    | Koem Kab              | 38629.32    |
| 2023-08    | Koem Kab              | 19210.3     |
| 2023-09    | Koem Kab              | 10105.74    |
| 2023-10    | Noah's Second Country | 35270.02    |
| 2023-11    | Aerilia               | 12785.81    |
| 2023-12    | Varanius              | 17699.61    |

#### Number of Unique Cards Traded Each Month

| Month   | Unique Cards Traded |
|---------|----------------------|
| 2023-01 | 100018               |
| 2023-02 | 80047                |
| 2023-03 | 87552                |
| 2023-04 | 66876                |
| 2023-05 | 82923                |
| 2023-06 | 74682                |
| 2023-07 | 73707                |
| 2023-08 | 72355                |
| 2023-09 | 68646                |
| 2023-10 | 63947                |
| 2023-11 | 68737                |
| 2023-12 | 69452                |

#### Top 3 Legendaries By Bank Each Month

> January 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S2 S_diego              | 7827.41           |
| S3 Racoda               | 3149.99           |
| S3 Crazy girl           | 2061.03           |

> February 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S2 S_diego              | 2608.02           |
| S3 Giovanniland         | 1864.48           |
| S3 Sedgistan            | 1707.78           |

> March 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S2 Sacara               | 5349.96           |
| S2 Lamoni               | 2479.53           |
| S3 Chan Island          | 2083.33           |

> April 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S3 Morover              | 4444.67           |
| S3 Sedgistan            | 2529.5            |
| S3 Noahs Second Country | 1800.99           |

> May 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S3 Testlandia           | 2521.65           |
| S3 Crazy girl           | 2280.0            |
| S3 Giovanniland         | 2157.0            |

> June 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S3 Sedgistan            | 1475.99           |
| S3 Wrapper              | 1464.99           |
| S3 Verdant Haven        | 1174.93           |

> July 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S3 Racoda               | 1602.47           |
| S3 Sedgistan            | 1552.65           |
| S3 Chan Island          | 1500.0            |

> August 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S3 Annihilators of Chan Island | 15000.5    |
| S3 Chan Island          | 3500.0            |
| S3 Sylh Alanor          | 3418.5            |

> September 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S3 Annihilators of Chan Island | 10000.0    |
| S3 The Stalker          | 3850.12           |
| S3 Daarwyrth            | 2060.5            |

> October 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S3 Annihilators of Chan Island | 9999.99    |
| S3 Safj                 | 3607.5            |
| S3 Alice Gardens        | 2296.37           |

> November 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S3 Annihilators of Chan Island | 5000.0     |
| S3 Morover              | 4500.0            |
| S1 Eaischpnaeieacgkque Bhcieaghpodsttditf | 3263.0 |

> December 2023

| Card Name               | Total Money Moved |
|-------------------------|-------------------|
| S2 Sacara               | 13184.04          |
| S3 The Stalker          | 8993.53           |
| S3 Morover              | 2955.02           |
