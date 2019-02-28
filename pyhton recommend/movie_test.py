import pandas as pd 

# Get the data 
column_names = ['user_id', 'item_id', 'rating', 'timestamp'] 
path = 'https://cdncontribute.geeksforgeeks.org/wp-content/uploads/file.tsv'

# Check the head of the data 
df = pd.read_csv(path, sep='\t', names=column_names) 
#print(df.head()) 

movie_titles = pd.read_csv('https://cdncontribute.geeksforgeeks.org/wp-content/uploads/Movie_Id_Titles.csv') 

#print(movie_titles.head())

data = pd.merge(df, movie_titles, on='item_id') 
#print(data.head()) 

# Calculate mean rating of all movies 
#print(data.groupby('title')['rating'].mean().sort_values(ascending=False).head() )

# Calculate count rating of all movies 
#print(data.groupby('title')['rating'].count().sort_values(ascending=False).head() )     

# creating dataframe with 'rating' count values 
ratings = pd.DataFrame(data.groupby('title')['rating'].mean()) 

ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count()) 

#print(ratings.head()) 
# Sorting values according to 
# the 'num of rating column' 
moviemat = data.pivot_table(index ='user_id',columns ='title', values ='rating') 

print(moviemat.head()) 

print(ratings.sort_values('num of ratings', ascending = False).head(10)) 




