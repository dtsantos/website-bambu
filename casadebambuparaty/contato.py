import webapp2
import cgi
from google.appengine.api import users
from google.appengine.api import mail

class MainPage(webapp2.RequestHandler):
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
  	<meta name="keywords" content="paraty, hosting, hotel, hostel, pousada, cheap, house, bambu, groups, trips, local, carnaval, new year, boat" />

	<title>Bambu House Contact - Paraty</title>

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
			<img src="img/head.jpg" alt="Header Bambu" width="960" height="100" />
			<div class="wifi">
				<img src="img/wifi.gif" width="60" height="24" alt="Disponibilizamos Internet Wi-Fi" />
			</div>
			<div class="opcoes">
				<ul>
					<li><a href="index.html">Inicio</a></li>
					<li><a href="casa.html">Casa</a></li>
					<li><a href="quartos.html">Quartos</a></li>
					<li><a href="contato.html">Contato</a></li>
				</ul>
			</div> 

			<div class="flags">
				<ul>
					<li>
						<a href="contato.en.html">
							<img src="img/flag_en.gif" width="26" height="18" alt="English Version" />
						</a>
					</li>
				</ul>
			</div>
		</header>
		
		<div class="container-contato">
			<h1>Casa de Bambu</h1>
			<h2>Contato</h2>

			<div id="#centered-text">
				<p>Preencha o formulario abaixo e entraremos em contato em breve:</p>
			</div>
			
			<form action="/confirmacao.html" method="post">
                <table style="margin-left: 270px; font-size: 12;" >
 				<tr>
				  <td align="left"><label for="usr">Nome:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="nome" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">Telefone:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="tel" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">E-mail:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="email" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">Mensagem:</label>&nbsp;
				  </td>
  				  <td><textarea name="msg" rows="8" cols="40"></textarea></td>
  				
				  <td></td> 
			 	</tr>
			 	<tr>
			 	 <td>
			 	 </td>
			 	 <td align="center"><input type="submit" value="  Enviar  "></td>
			 	</tr>
				</table>
    		</form>
    		<p>A hospedaria situa-se paralelo a BR 101, no ponto A, conforme mapa abaixo</p>
				<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=d&amp;source=s_d&amp;saddr=-23.226124,-44.727491&amp;daddr=&amp;hl=en&amp;geocode=&amp;sll=-23.221904,-44.721565&amp;sspn=0.016446,0.028882&amp;mra=mift&amp;mrsp=0&amp;sz=16&amp;ie=UTF8&amp;ll=-23.221904,-44.721565&amp;spn=0.016446,0.028882&amp;t=m&amp;output=embed">
				</iframe>
				<br/>
				<small>
					<a href="https://maps.google.com/maps?f=d&amp;source=embed&amp;saddr=-23.226124,-44.727491&amp;daddr=&amp;hl=en&amp;geocode=&amp;sll=-23.221904,-44.721565&amp;sspn=0.016446,0.028882&amp;mra=mift&amp;mrsp=0&amp;sz=16&amp;ie=UTF8&amp;ll=-23.221904,-44.721565&amp;spn=0.016446,0.028882&amp;t=m" style="color:#0000FF;text-align:left">
					<br>Visualizar Mapa Grande</a>
				</small><br><br>
			</p>
		</div>
				
		<footer>
			<img src="img/foot.jpg" alt="Footer Bambu" width="480" height="100"><img src="img/foot.jpg" alt="Footer Casa de Bambu" width="480" height="100">
			<p>Hospedaria Casa de Bambu - Rua B, Vila D. Pedro I - Paraty - RJ - Brasil </p>
			<p>fpnsantos@gmail.com - +55 (24) 3371-0365 </p>
		</footer>

	</div>
</body>
</html>

      """)

class Confirmacao(webapp2.RequestHandler):
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

	<title>Bambu House Home - Paraty</title>

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
			<img src="img/head.jpg" alt="Header Bambu" width="960" height="100" />
			<div class="wifi">
				<img src="img/wifi.gif" width="60" height="24" alt="Disponibilizamos Internet Wi-Fi" />
			</div>
			<div class="opcoes">
				<ul>
					<li><a href="index.html">Inicio</a></li>
					<li><a href="casa.html">Casa</a></li>
					<li><a href="quartos.html">Quartos</a></li>
					<li><a href="contato.html">Contato</a></li>
				</ul>
			</div> 

			<div class="flags">
				<ul>
					<li>
						<a href="contato.en.html">
							<img src="img/flag_en.gif" width="26" height="18" alt="English Version" />
						</a>
					</li>
				</ul>
			</div>
		</header>
		
		<div class="container-contato">
			<h1>Mensagem Enviada</h1>

			<div id="#centered-text">
				<p>Obrigado por seu contato! Responderemos a sua consulta em ate 24 horas.</p>
				<p>Segue nosso endereco:
				<p>Hospedaria Casa de Bambu</p>
  				<p>Rua B, Vila D. Pedro I - Paraty - RJ - Brasil</p>
				<p>A hospedaria situa-se paralelo a BR 101, no ponto A, conforme mapa abaixo</p>
				<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=d&amp;source=s_d&amp;saddr=-23.226124,-44.727491&amp;daddr=&amp;hl=en&amp;geocode=&amp;sll=-23.221904,-44.721565&amp;sspn=0.016446,0.028882&amp;mra=mift&amp;mrsp=0&amp;sz=16&amp;ie=UTF8&amp;ll=-23.221904,-44.721565&amp;spn=0.016446,0.028882&amp;t=m&amp;output=embed">
				</iframe>
				<br/>
				<small>
					<a href="https://maps.google.com/maps?f=d&amp;source=embed&amp;saddr=-23.226124,-44.727491&amp;daddr=&amp;hl=en&amp;geocode=&amp;sll=-23.221904,-44.721565&amp;sspn=0.016446,0.028882&amp;mra=mift&amp;mrsp=0&amp;sz=16&amp;ie=UTF8&amp;ll=-23.221904,-44.721565&amp;spn=0.016446,0.028882&amp;t=m" style="color:#0000FF;text-align:left">
					<br>Visualizar Mapa Grande</a>
				</small><br><br>
			</p>
			</div>
		</div>
		
		<footer>
			<img src="img/foot.jpg" alt="Footer Bambu" width="480" height="100"><img src="img/foot.jpg" alt="Footer Casa de Bambu" width="480" height="100">
			<p>Hospedaria Casa de Bambu - Rua B, Vila D. Pedro I - Paraty - RJ - Brasil </p>
			<p>fpnsantos@gmail.com - +55 (24) 3371-0365 </p>
		</footer>

	</div>
</body>
</html>

      """)
	

      
app = webapp2.WSGIApplication([('/contato.html', MainPage),
                              ('/confirmacao.html', Confirmacao)],
                              debug=True)