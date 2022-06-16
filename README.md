# fast-url
Build a URL Shortener With FastAPI and Python


| Endpoint 	            |   HTTP Verb 	    | Request Body 	            |         Action                                                                |
| :---:                 |     :---:         |               :---:       |                          :---:                                                |
| / 	                |     GET 		    |                           | Returns a Hello, World! string                                                |
| /url 	                |     POST 	        | Your target URL 	        | Shows the created url_key with additional info, including a secret_key        |
| /{url_key} 	        |     GET 		    |                           | Forwards to your target URL                                                   |
| /admin/{secret_key} 	|     GET 		    |                           | Shows administrative info about your shortened URL                            |
| /admin/{secret_key} 	|    DELETE 	    | Your secret key 	        | Deletes your shortened URL                                                    |

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |

# Aimed response body: 
{
  "target_url": "https://realpython.com",
  "is_active": true,
  "clicks": 0,
  "url": "JNPGB",
  "admin_url": "MIZJZYVA"
}
