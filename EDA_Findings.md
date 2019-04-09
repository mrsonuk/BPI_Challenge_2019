

# VARIABLE SPECIFICATION (description, unique values)
  -   eventID                           - identifier for events (n=1595923)                       int64
-   case Spend area text              - type/class of purchase item (n=21)                      object
-   case Company                      - company from which purchase originated (n=4)            object
-   case Document Type                - type of order in the case (n=3)                         object
-   case Sub spend area text          - type of purchase item (n=136)                           object
-   case Purchasing Document          - identifier for cases/purchases (n=76349)                int64
-   case Purch. Doc. Category name    - category of purchase document (n=1)                     object
-   case Vendor                       - vendor to which purchase document is sent (n=1975)      object
-   case Item Type                    - purchase classification (n=6)                           object
-   case Item Category                - purchase main document category (n=4)                   object
-   case Spend classification text    - purchase type classification (n=3)                      object
-   case Source                       - system from purchase originated (n=1)                   object
-   case Name                         - name/vendor of purchase (n=1899)                        object
-   case GR-Based Inv. Verif.         - case Goods Received invoice verification (n=2)          bool
-   case Item                         - item type (n=490)                                       int64
-   case concept:name                 - case identifier (n=251734)                              object
-   case Goods Receipt                - flag indicating if 3 way matching is required (n=2)     bool
-   event User                        - user identifier of the event (n=628)                    object
-   event org:resource                - DUPLICATE user identifier of the event (n=628)          object
-   event concept:name                - event name/type (n=42)                                  object
-   event Cumulative net worth (EUR)  - cost of purchase at the time of the event (n=25221)     float64
-   event time:timestamp              - timestamp of the event (n=167432)                       object


# VARIABLES WITH MISSING VALUES:
 3289 cases, with missing values for each variable in 16294 events
Missing variables:
-     - case Spend area text
-     - case Sub spend area text
-     - case Spend classification text
    
 For each case with missing values, each activity in this case has these values missing
 
1.     Filled these columns for missing values with "Other"
1.     Keep cases because missing does not imply faulty data
1.     Missing of these values might be relevant predictor itself

# EDA:
1. Bar plots were created for categorical variables. Insights:
1.   Company0000 occurs way more often than any other variable
1.   Document Standard PO occurs way more often than Framework order an EC Purchase Other
1.   Goods receipt = False almost never occurs, which means that the third category (2-way matching) almost never occurs,
 as can be seen at the case item category distribution as well
1.   more can be seen in FiguresEDA
