import webapp2
import cgi
from google.appengine.api import users
from google.appengine.api import mail

class MainPageEn(webapp2.RequestHandler):
  def get(self):
      self.response.out.write("""

<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
<head>
	<meta charset="UTF-8" content="text/html" />
  	<meta name="description" content="Hosting for couples or groups in Paraty in an environment surrounded by a garden filled with Atlantic Forest species at a bambu made house. We are a local family and will help you with tips of what to do and much more! Great prices!" />
  	<meta name="keywords" content="paraty, hosting, hotel, pousada, cheap, house, bambu, groups, trips, local, carnaval, new year, boat" />

	<title>Bambu House Paraty - Contact Page</title>

	<meta name="viewport" content="width=device-width">
	<link rel="stylesheet" href="css/normalize.css">
	<link rel="stylesheet" href="css/style.css" />
	<script src="js/script.js"></script>
    <script>
            var _gaq=[['_setAccount','UA-38332351-1'],['_trackPageview']];
            (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
            g.src='//www.google-analytics.com/ga.js';
            s.parentNode.insertBefore(g,s)}(document,'script'));
    </script>
</head>
<body>
	<div class="wrap">
		<header>
			<img src="img/head.jpg" alt="Header Bambu" width="960" height="50" />
			<div class="wifi">
				<img src="img/wifi.gif" width="60" height="24" alt="We offer Wi-Fi Internet" />
			</div>
			<div class="opcoes">
				<ul>
					<li><a href="index.en.html">Home</a></li>
					<li><a href="casa.en.html">House</a></li>
					<li><a href="quartos.en.html">Rooms</a></li>
					<li><a href="contato.en.html">Contact</a></li>
				</ul>
			</div> 

			<div class="flags">
				<ul>
					<li>
						<a href="contato.html">
							<img src="img/flag_pt.gif" width="26" height="18" alt="Versao em Portugues" />
						</a>
					</li>
				</ul>
			</div>
		</header>
		
		<div class="container-contato">
			<h1>Bambu House</h1>
			<h2>Contact</h2>
			<p>
				Get in touch with us through phone (+55 24):
			</p>
			<p>
					3371-0365 Fixo | 9975-7859 Vivo | 8130-2503 TIM |
					9204-6039 Claro | 8835-5643 OI
				</p>
			<div class="simple-images">
				<p>Or fill in the form and we will get in touch with you soon:</p>
			</div>
			
			<form action="/confirmacao.en.html" method="post">
                <table style="margin-left: 270px; font-size: 12;" >
 				<tr>
				  <td align="left"><label for="usr">Name:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="nome" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">Telephone:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="tel" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">E-mail:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="email" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">Message:</label>&nbsp;
				  </td>
  				  <td><textarea id="mensagem"name="msg" rows="8" cols="40"></textarea></td>
  				
				  <td></td> 
			 	</tr>
			 	<tr>
			 	 <td>
			 	 </td>
			 	 <td align="center"><input type="submit" value="  Enviar  "></td>
			 	</tr>
				</table>
    		</form>
			<!-- Checking if an email was typed -->
			<script>prepareEventHandlers("Please fill in the e-mail and message fields");</script>
			<p><span id="errorMessage"></span></p>
    		<p>Our house is situated parallel to BR 101, at point A, according to the map bellow</p>
				<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=d&amp;source=s_d&amp;saddr=-23.226124,-44.727491&amp;daddr=&amp;hl=en&amp;geocode=&amp;sll=-23.221904,-44.721565&amp;sspn=0.016446,0.028882&amp;mra=mift&amp;mrsp=0&amp;sz=16&amp;ie=UTF8&amp;ll=-23.221904,-44.721565&amp;spn=0.016446,0.028882&amp;t=m&amp;output=embed">
				</iframe>
				<br/>
				<small>
					<a href="https://maps.google.com/maps?f=d&amp;source=embed&amp;saddr=-23.226124,-44.727491&amp;daddr=&amp;hl=en&amp;geocode=&amp;sll=-23.221904,-44.721565&amp;sspn=0.016446,0.028882&amp;mra=mift&amp;mrsp=0&amp;sz=16&amp;ie=UTF8&amp;ll=-23.221904,-44.721565&amp;spn=0.016446,0.028882&amp;t=m" style="color:#0000FF;text-align:left">
					<br>Open Full Page Map</a>
				</small><br><br>
			</p>
		</div>
				
		<footer>
			<img src="img/foot.jpg" alt="Footer Bambu" width="480" height="50"><img src="img/foot.jpg" alt="Footer Casa de Bambu" width="480" height="50">
			<p>Hospedaria Casa de Bambu - Rua B, Vila D. Pedro I - Paraty - RJ - Brasil </p>
			<p>fpnsantos@gmail.com - +55 (24) 3371-0365 </p>
		</footer>

	</div>
</body>
</html>

      """)

class ConfirmacaoEn(webapp2.RequestHandler):
    def post(self):
    	message = mail.EmailMessage(sender="Davi Trindade <davitrindade@gmail.com>",
                            subject="Consulta Casa de Bambu: "+self.request.get('nome'),to="fpnsantos@gmail.com",reply_to=" "+self.request.get('nome')+" <"+self.request.get('email')+">",
                            body="Remetente: "+self.request.get('nome')+"\nTelefone: "+self.request.get('tel')+"\nEmail: "+self.request.get('email')+"\nMensagem: \n"+self.request.get('msg'))
	message.send()
	
	self.response.out.write("""

<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
<head>
	<meta charset="UTF-8" content="text/html" />
  	<meta name="description" content="Hosting for couples or groups in Paraty in an environment surrounded by a garden filled with Atlantic Forest species at a bambu made house. We are a local family and will help you with tips of what to do and much more! Great prices!" />
  	<meta name="keywords" content="paraty, hosting, hotel, pousada, cheap, house, bambu, groups, trips, local, carnaval, new year, boat" />

	<title>Bambu House Paraty - Contact Page</title>

	<meta name="viewport" content="width=device-width">
	<link rel="stylesheet" href="css/normalize.css">
	<link rel="stylesheet" href="css/style.css" />
    <script>
            var _gaq=[['_setAccount','UA-38332351-1'],['_trackPageview']];
            (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
            g.src='//www.google-analytics.com/ga.js';
            s.parentNode.insertBefore(g,s)}(document,'script'));
    </script>
</head>

<body>
	<div class="wrap">
		<header>
			<img src="img/head.jpg" alt="Header Bambu" width="960" height="50" />
			<div class="wifi">
				<img src="img/wifi.gif" width="60" height="24" alt="We offer Wi-Fi Internet" />
			</div>
			<div class="opcoes">
				<ul>
					<li><a href="index.en.html">Home</a></li>
					<li><a href="casa.en.html">House</a></li>
					<li><a href="quartos.en.html">Rooms</a></li>
					<li><a href="contato.en.html">Contact</a></li>
				</ul>
			</div> 

			<div class="flags">
				<ul>
					<li>
						<a href="contato.html">
							<img src="img/flag_pt.gif" width="26" height="18" alt="Versao em Portugues" />
						</a>
					</li>
				</ul>
			</div>
		</header>
        
		
		<div class="container-contato">
			<h1>Message sent!</h1>

			<div class="simple-images">
			<p>
				Get in touch with us through phone (+55 24):
			</p>
			<p>
					3371-0365 Fixo | 9975-7859 Vivo | 8130-2503 TIM |
					9204-6039 Claro | 8835-5643 OI
				</p>
				<p>Thank you for your message! We will answer your enquire in maximum 24 hours.</p>
				<p>This is our address:
				<p>Hospedaria Casa de Bambu</p>
  				<p>Rua B, Vila D. Pedro I - Paraty - RJ - Brasil</p>
				<p>Our house is situated parallel to BR 101, at point A, according to the map bellow</p>
				<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=d&amp;source=s_d&amp;saddr=-23.226124,-44.727491&amp;daddr=&amp;hl=en&amp;geocode=&amp;sll=-23.221904,-44.721565&amp;sspn=0.016446,0.028882&amp;mra=mift&amp;mrsp=0&amp;sz=16&amp;ie=UTF8&amp;ll=-23.221904,-44.721565&amp;spn=0.016446,0.028882&amp;t=m&amp;output=embed">
				</iframe>
				<br/>
				<small>
					<a href="https://maps.google.com/maps?f=d&amp;source=embed&amp;saddr=-23.226124,-44.727491&amp;daddr=&amp;hl=en&amp;geocode=&amp;sll=-23.221904,-44.721565&amp;sspn=0.016446,0.028882&amp;mra=mift&amp;mrsp=0&amp;sz=16&amp;ie=UTF8&amp;ll=-23.221904,-44.721565&amp;spn=0.016446,0.028882&amp;t=m" style="color:#0000FF;text-align:left">
					<br>Open Full Page Map</a>
				</small><br><br>
			</p>
			</div>
		</div>
		
		<footer>
			<img src="img/foot.jpg" alt="Footer Bambu" width="480" height="50"><img src="img/foot.jpg" alt="Footer Casa de Bambu" width="480" height="50">
			<p>Hospedaria Casa de Bambu - Rua B, Vila D. Pedro I - Paraty - RJ - Brasil </p>
			<p>fpnsantos@gmail.com - +55 (24) 3371-0365 </p>
		</footer>

	</div>
</body>
</html>

      """)
	

      
app = webapp2.WSGIApplication([('/contato.en.html', MainPageEn),
                              ('/confirmacao.en.html', ConfirmacaoEn)],
                              debug=True)