import seaborn
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("BPI_Challenge_2019.csv", encoding='ANSI', engine="c")
# some clumns have whitespaces in keywords - remove them:
data.columns = data.columns.str.strip()

# MISSING VALUES
missing_vars = ['case Spend area text',
                'case Sub spend area text', 'case Spend classification text']

len(data[data[missing_vars[0]].isnull() == True])
len(data[data[missing_vars[1]].isnull() == True])
len(data[data[missing_vars[2]].isnull() == True])

case_missing_1 = data[data[missing_vars[0]].isnull() == True]["case concept:name"].unique()
case_missing_2 = data[data[missing_vars[1]].isnull() == True]["case concept:name"].unique()
case_missing_3 = data[data[missing_vars[2]].isnull() == True]["case concept:name"].unique()


activity_missing_1 = data[data[missing_vars[0]].isnull() == True]["eventID"].unique()
activity_missing_2 = data[data[missing_vars[1]].isnull() == True]["eventID"].unique()
activity_missing_3 = data[data[missing_vars[2]].isnull() == True]["eventID"].unique()


missing_data = data[data[missing_vars[0]].isnull() == True]
non_missing_data = data[data[missing_vars[0]].isnull() == False]

missing_event_categories = missing_data["event concept:name"].value_counts() / missing_data.shape[0]
non_missing_event_categories = non_missing_data["event concept:name"].value_counts() / non_missing_data.shape[0]

event_category_value_counts = pd.DataFrame(
    {"missing_data": missing_event_categories, "non_missing_data": non_missing_event_categories})
event_category_value_counts.fillna(0, inplace=True)
(event_category_value_counts["missing_data"] /
 event_category_value_counts["non_missing_data"]).sort_values(ascending=False)

missing_case_ids = missing_data['case concept:name'].unique()

for id in missing_case_ids[:100]:
    subset = data[data["event concept:name"] == id]['case Spend area text']
    if subset.isnull().sum() == subset.shape[0]:
        print("AA")


# missing variables
# 1 variable missing everywhere in the case
# 2 variable dependent on "event concept:name"
# 3 variable dependent on "case Item Category"


# EXPLORATORY DATA ANALYSIS
# stats for numeric vars
data.describe()
#
exclude = ['eventID', 'case Purchasing Document', 'case Item',
           'event Cumulative net worth (EUR)', 'case concept:name', 'event time:timestamp', 'case Vendor', 'case Name']

c = ''
for c in data.columns:
    if c not in exclude:
        # print(data[c].value_counts())
        plt.figure(), data[c].value_counts().plot(kind='bar'), plt.title(c), plt.savefig(dpi = 300, fname = "figure" )
