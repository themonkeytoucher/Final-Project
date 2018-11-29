
import urllib.request, json 

"""
Author: Anthony Tom
Input: the item's id
Output: A dictionary of the item's catalogue info
Example:
{  
   "item":{  
      "icon":"http://services.runescape.com/m=itemdb_rs/4908_obj_sprite.gif?id=4151",
      "icon_large":"http://services.runescape.com/m=itemdb_rs/4908_obj_big.gif?id=4151",
      "id":4151,
      "type":"Default",
      "typeIcon":"http://www.runescape.com/img/categories/Default",
      "name":"Abyssal whip",
      "description":"A weapon from the abyss.",
      "current":{  
         "trend":"neutral",
         "price":"2.3m"
      },
      "today":{  
         "trend":"neutral",
         "price":0
      },
      "members":"true",
      "day30":{  
         "trend":"positive",
         "change":"+9.0%"
      },
      "day90":{  
         "trend":"negative",
         "change":"-7.0%"
      },
      "day180":{  
         "trend":"positive",
         "change":"+44.0%"
      }
   }
}

This is the general info of an item, not the specifics of a graph
"""
def get_catalogue(item_id):
	url = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=%d" %item_id
	with urllib.request.urlopen(url) as url:
	    data = json.loads(url.read().decode())
	    return data

"""
Author: Anthony Tom
Input: Item ID
Output: A dictionary of the item's day to day price points on a graph
Example:
{
	'daily':{
		'1527897600000': 181,
		'1527984000000': 180,
		'1528070400000': 180,
		'1528156800000': 182,
		...
	}
	'average':{
		'1527897600000': 186, 
		'1527984000000': 186, 
		'1528070400000': 186, 
		'1528156800000': 186, 
		'1528243200000': 186,
		...
	}
}
"""
def get_graph(item_id):
	url = "http://services.runescape.com/m=itemdb_oldschool/api/graph/%d.json" %item_id
	with urllib.request.urlopen(url) as url:
	    data = json.loads(url.read().decode())
	    return data

if __name__ == "__main__":
	catalogue = get_graph(2)
	print(catalogue['average'])
