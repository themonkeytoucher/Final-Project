
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
	 '1527897600000': 181,
	 '1527984000000': 180,
	 '1528070400000': 180,
	 '1528156800000': 182,
	 '1528243200000': 188,
	 '1528329600000': 189,
	 '1528416000000': 189,
	 '1528502400000': 191,
	 '1528588800000': 196,
	 '1528675200000': 203,
	 '1528761600000': 209,
	 '1528848000000': 214,
	 '1528934400000': 217,
	 '1529020800000': 221,
	 '1529107200000': 224,
	 '1529193600000': 228,
	 '1529280000000': 235,
	 '1529366400000': 234,
	 '1529452800000': 228,
	 '1529539200000': 223,
	 '1529625600000': 214,
	 '1529712000000': 206,
	 '1529798400000': 202,
	 '1529884800000': 201,
	 '1529971200000': 200,
	 '1530057600000': 200,
	 '1530144000000': 199,
	 '1530230400000': 199,
	 '1530316800000': 201,
	 '1530403200000': 205,
	 '1530489600000': 211,
	 '1530576000000': 217,
	 '1530662400000': 224,
	 '1530748800000': 228,
	 '1530835200000': 229,
	 '1530921600000': 225,
	 '1531008000000': 216,
	 '1531094400000': 211,
	 '1531180800000': 209,
	 '1531267200000': 210,
	 '1531353600000': 208,
	 '1531440000000': 208,
	 '1531526400000': 209,
	 '1531612800000': 209,
	 '1531699200000': 215,
	 '1531785600000': 222,
	 '1531872000000': 229,
	 '1531958400000': 230,
	 '1532044800000': 230,
	 '1532131200000': 230,
	 '1532217600000': 227,
	 '1532304000000': 226,
	 '1532390400000': 228,
	 '1532476800000': 229,
	 '1532563200000': 230,
	 '1532649600000': 230,
	 '1532736000000': 225,
	 '1532822400000': 221,
	 '1532908800000': 218,
	 '1532995200000': 216,
	 '1533081600000': 214,
	 '1533168000000': 210,
	 '1533254400000': 210,
	 '1533340800000': 208,
	 '1533427200000': 207,
	 '1533513600000': 209,
	 '1533600000000': 213,
	 '1533686400000': 216,
	 '1533772800000': 219,
	 '1533859200000': 221,
	 '1533945600000': 221,
	 '1534032000000': 221,
	 '1534118400000': 221,
	 '1534204800000': 222,
	 '1534291200000': 220,
	 '1534377600000': 217,
	 '1534464000000': 211,
	 '1534550400000': 203,
	 '1534636800000': 196,
	 '1534723200000': 196,
	 '1534809600000': 202,
	 '1534896000000': 206,
	 '1534982400000': 210,
	 '1535068800000': 210,
	 '1535155200000': 207,
	 '1535241600000': 202,
	 '1535328000000': 199,
	 '1535414400000': 199,
	 '1535500800000': 201,
	 '1535587200000': 202,
	 '1535673600000': 207,
	 '1535760000000': 208,
	 '1535846400000': 206,
	 '1535932800000': 207,
	 '1536019200000': 210,
	 '1536105600000': 211,
	 '1536192000000': 212,
	 '1536278400000': 211,
	 '1536364800000': 210,
	 '1536451200000': 210,
	 '1536537600000': 209,
	 '1536624000000': 209,
	 '1536710400000': 209,
	 '1536796800000': 208,
	 '1536883200000': 208,
	 '1536969600000': 207,
	 '1537056000000': 207,
	 '1537142400000': 207,
	 '1537228800000': 207,
	 '1537315200000': 207,
	 '1537401600000': 206,
	 '1537488000000': 206,
	 '1537574400000': 207,
	 '1537660800000': 207,
	 '1537747200000': 208,
	 '1537833600000': 208,
	 '1537920000000': 206,
	 '1538006400000': 206,
	 '1538092800000': 205,
	 '1538179200000': 205,
	 '1538265600000': 205,
	 '1538352000000': 206,
	 '1538438400000': 206,
	 '1538524800000': 205,
	 '1538611200000': 204,
	 '1538697600000': 203,
	 '1538784000000': 199,
	 '1538870400000': 196,
	 '1538956800000': 199,
	 '1539043200000': 202,
	 '1539129600000': 204,
	 '1539216000000': 205,
	 '1539302400000': 205,
	 '1539388800000': 202,
	 '1539475200000': 199,
	 '1539561600000': 200,
	 '1539648000000': 202,
	 '1539734400000': 204,
	 '1539820800000': 207,
	 '1539907200000': 207,
	 '1539993600000': 207,
	 '1540080000000': 212,
	 '1540166400000': 214,
	 '1540252800000': 214,
	 '1540339200000': 211,
	 '1540425600000': 211,
	 '1540512000000': 211,
	 '1540598400000': 209,
	 '1540684800000': 208,
	 '1540771200000': 208,
	 '1540857600000': 209,
	 '1540944000000': 209,
	 '1541030400000': 209,
	 '1541116800000': 209,
	 '1541203200000': 209,
	 '1541289600000': 209,
	 '1541376000000': 210,
	 '1541462400000': 213,
	 '1541548800000': 218,
	 '1541635200000': 223,
	 '1541721600000': 221,
	 '1541808000000': 217,
	 '1541894400000': 215,
	 '1541980800000': 213,
	 '1542067200000': 213,
	 '1542153600000': 212,
	 '1542240000000': 211,
	 '1542326400000': 208,
	 '1542412800000': 205,
	 '1542499200000': 204,
	 '1542585600000': 204,
	 '1542672000000': 203,
	 '1542758400000': 204,
	 '1542844800000': 204,
	 '1542931200000': 203,
	 '1543017600000': 202,
	 '1543104000000': 200,
	 '1543190400000': 200,
	 '1543276800000': 201,
	 '1543363200000': 200
 }
"""
def get_graph(item_id):
	url = "http://services.runescape.com/m=itemdb_oldschool/api/graph/%d.json" %item_id
	with urllib.request.urlopen(url) as url:
	    data = json.loads(url.read().decode())
	    return data

if __name__ == "__main__":
	catalogue = get_graph(2)
	print(catalogue['daily'])
