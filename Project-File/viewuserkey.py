#!C:\Users\DELL-LAPTOP\AppData\Local\Programs\Python\Python37\python
import cgi
import mysql.connector
print("Content-type: text/html")
print("")
print("""
<html>

<head>
  <title>Security of Card using PUF and FRODO</title>
  <meta name="description" content="website description" />
  <meta name="keywords" content="website keywords, website keywords" />
  <meta http-equiv="content-type" content="text/html; charset=windows-1252" />
  <link rel="stylesheet" type="text/css" href="style/style.css" />
  <meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    text-align: left;
    padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

th {
    background-color: #4CAF50;
    color: white;
}
</style>
</head>

<body>
  <div class="w3-top">
  <div class="w3-bar w3-black w3-card">
    <a class="w3-bar-item w3-button w3-padding-large w3-hide-medium w3-hide-large w3-right" href="javascript:void(0)" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
    <a href="adminhome.html" class="w3-bar-item w3-button w3-padding-large">HOME</a> 
 <a href="viewuserkey.py" class="w3-bar-item w3-button">User Key</a>    
<a href="adminhome.html" class="w3-bar-item w3-button w3-padding-large">Logout</a>
    <h5 align="center"><strong>Securing <span class="logo_colour"> the Card Using Puf</strong></span></h5>
  </div>
</div>  
<div class="w3-content" style="max-width:2000px;margin-top:46px">

  <!-- Automatic Slideshow Images -->
  <div class="w3-display-container w3-center">
    <img src="images/credit2.jpg" style="height:600px","width:100%">
    <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
       <h1>Welcome to securing Card transaction</h1>
        <p>Welcome To Admin Home...
		</p>   
    </div>
  </div>
  </div><br><br> 
    <table>
  <tr>
    <th>Name</th>
    <th>Password</th>
    <th>Card No.</th>
	<th>Bank</th>
    <th>Branch</th>
    <th>Phone</th>
	<th>Private Key</th>
    <th>Key</th>
  </tr>""")
con = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='shravya');
if(con):
    #print("connected");
    c = con.cursor()
    q = "select * from user"
    c.execute(q,)
    output=c.fetchall()
    #print(output)
for row in output:
        
	print("<tr>");
	print("<td>",row[1],"</td>")
	print("<td>",row[3],"</td>")
	print("<td>",row[9],"</td>")	
	print("<td>",row[4],"</td>")
	print("<td>",row[5],"</td>")
	print("<td>",row[6],"</td>")
	print("<td>",row[14],"</td>")
	print("<td>",row[15],"</td>")
   
	print("</tr>");
print("<table>");

print("""
</div>
    </div>
    <div id="content_footer"></div>
    <div id="footer">
      <center><p><a href="adminhome.html">Home</a> | <a href="viewuserkey.py">User Key</a> | <a href="shravya.html">Logout</a></p>
        
        
  </div>
</body>
</html>
""");
