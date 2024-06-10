import pandas as pd
import csv
from collections import Counter
from itertools import islice
from operator import itemgetter



df = pd.read_csv('ssense_dataset.csv')

df.to_pound = df.price_usd*0.78

colors = [
    "red", "blue", "green", "yellow", "black", "white", "orange", "purple", "pink",
    "brown", "gray", "grey", "violet", "indigo", "turquoise", "magenta", "cyan",
    "beige", "lavender", "maroon", "olive", "peach", "teal", "navy", "gold", "silver",
    "bronze", "coral", "burgundy", "ivory", "khaki", "lime", "mustard", "tan",
    "salmon", "charcoal", "emerald", "sapphire", "ruby", "amber", "mint", "aqua",
    "cream", "fuchsia", "periwinkle", "mauve", "ochre", "plum", "sand", "copper",
    "chocolate", "raspberry", "saffron", "jade", "azure", "amethyst", "brass",
    "crimson", "denim", "ebony", "flax", "lilac", "pearl", "rose", "rust", "sepia",
    "smoke", "tangerine", "topaz", "ultramarine", "vermilion", "wheat", "zinc",
    "aquamarine", "blush", "cobalt", "ecru", "eggshell", "garnet", "honey",
    "mahogany", "midnight blue", "mulberry", "pewter", "sage", "scarlet", "seafoam",
    "slate", "steel", "terracotta", "vanilla"
]

color_list = []
color_counter = []

def count_colors(df, colors):
    color_list = []

    if 'description' in df.columns:
        for desc in df['description'].astype(str):
            for color in colors:
                if color.lower() in desc.lower():  
                    color_list.append(color)
        
        
            
        return color_list
       
def sort_colors(color_list):
    color_counter = Counter(color_list)
    return color_counter

def popular_colors(d, n=10):
    most_popular_colors = dict(islice(d.items(), n))
    
    return most_popular_colors

    
def popular(color_counter, N):

    color_counter = Counter(color_list)
    most_common_colors = color_counter.most_common(N)
    print(f'These are the most popular colors sold at Ssense: ' + str(most_common_colors))


    most_popular_color2 = dict(sorted(color_counter.items(), key=itemgetter(1), reverse=True)[:N])

    
    
    
    return most_common_colors


def men(df):
    mens_df = df[df['type'] == 'mens']
    print(f'There are {len(mens_df.index)} unique menswear items sold at ssense')

    popular_brands_m = mens_df['brand'].value_counts().head(10)

    least_popular_brands_m = mens_df['brand'].value_counts().nsmallest(10)
    print(f'These are the least popular brands sold at Ssense ' + least_popular_brands_m)
    print(f'These are the most popular brands sold at Ssense ' + popular_brands_m)
    count_colors(mens_df, colors)

    return mens_df


def women(df):
    women_df = df[df['type'] == 'womens']
    print(f'There are {len(women_df.index)} unique womenswear items sold at ssense')
    popular_brands_f = women_df['brand'].value_counts().head(10)
    least_popular_brands_f = women_df['brand'].value_counts().nsmallest(10)
    print(least_popular_brands_f)
    return women_df



def brands(df):
    brands = df['brand'].unique()
    print(f"There are {brands} unique brands sold at ssense.")
    brands_list = brands.tolist()
    return brands_list

found_colors = count_colors(df, colors)
sort_colors(color_list)

color_list = count_colors(df, colors)
color_counter = sort_colors(color_list)
print(color_counter)

popular(color_counter, 5)
