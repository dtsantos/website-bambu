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
	<meta charset="UTF-8" />
  	<meta name="description" content="Hospedagem para casais ou grupos na cidade de Paraty em um ambiente cercado de um jardim com especies da mata atlantica em uma casa feita de Bambu. Somos uma familia local e tambem ajudamos com dicas de passeios e muito mais! Otimos precos!" />
  	<meta name="keywords" content="paraty, hospedagem, hotel, pousada, barata, casa, bambu, grupos, passeios, local, carnaval, reveillon, passeio, barco" />

	<title>Bambu House Contact - Paraty</title>

	<meta name="viewport" content="width=device-width">
	<link rel="stylesheet" href="css/normalize.css">
	<link rel="stylesheet" href="css/style.css" />
	<link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/themes/smoothness/jquery-ui.min.css" />
	
	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
	<script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>	
	<script src="js/script.js"></script>
    <script>
			$( document ).tooltip();
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
				<img src="img/wifi.gif" width="60" height="24" alt="Disponibilizamos Internet Wi-Fi" />
			</div>
			<div class="opcoes">
				<ul>
				<li><a href="index.html">inicio</a></li>
				<li><a href="casa.html">casa</a></li>
				<li><a href="quartos.html">quartos</a></li>
				<li><a href="faq.html">faq</a></li>
				<li><a href="contato.html">contato</a></li>
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
			<h1>Contato</h1>
			
			<form id="frmContact" action="/confirmacao.html" method="post">
				<fieldset>
				  <legend>Consulta:</legend>
				  <p>
					<label class="field" for="usr">Nome:&nbsp;</label>
					<input id="usr" placeholder="Seu Nome" type="text" name="nome" class="textbox"/>
				  </p>
				
				
				<p>
				  <label class="field" for="usr">Periodo:&nbsp;</label>
				  <input type="text" placeholder="Chegada" id="dataEntrada" name="dataEntrada" class="textbox-date" />
					<label class="field-middle" for="usr">a:&nbsp;</label>
					<input type="text" placeholder="Saida" id="dataSaida" name="dataSaida" class="textbox-date" />
				</p>
				
				
				<p>
					<label class="field-hospedes" for="hospedes">Hospedes:&nbsp;</label>
					<select class="textbox-option" id="hospedes" name="hospedes"> 
						<option value="1">1</option>
						<option value="2" selected="selected">2</option>
						<option value="3">3</option>
						<option value="4">4</option>
						<option value="5">5</option>
						<option value="6">6</option>
						<option value="7">7</option>
						<option value="8">8</option>
						<option value="9">9</option>
						<option value="10">10</option>	
						<option value="11">11</option>	
						<option value="12">12</option>	
					</select>
					<label class="field-kids" for="usr">&nbsp;&nbsp;Criancas:&nbsp;</label>
					<select class="textbox-option" id="criancas" name="criancas" title="Criancas ate 6 anos"> 
					    <option value="0">0</option>
						<option value="1">1</option>
						<option value="2">2</option>
						<option value="3">3</option>
						<option value="4">4</option>
						<option value="5">5</option>
						<option value="6">6</option>
						<option value="7">7</option>
						<option value="8">8</option>
						<option value="9">9</option>
					</select>
				</p> 
				
				<p>
					<label class="field" for="usr">E-mail:&nbsp;</label>
				 	<input id="email" placeholder="seu@email.com" class="textbox" name="email" />
				</p>
				<p>
					<label class="field" for="usr">Detalhes:&nbsp;</label>
				  	<textarea id="mensagem" placeholder="Algum detalhe sobre sua consulta" name="msg" rows="5" cols="28"></textarea>
				</p>
				<span id="errorMessage"></span>
			 		<div class="buttonHolder">
						<input type="submit" value="  Enviar  "/>
					</div>
				</fieldset>
    		</form>

			<!-- Checking if an email was typed -->
			<script>prepareEventHandlers("Infome suas datas e e-mail");</script>
				<p>Consulte datas ou ligue:
					(24) 3371-0365 ou
					<select id="telefones" title="Operadora"> 
					    <option value="9975-7859" selected="selected">Vivo</option>
						<option value="8130-2503">TIM</option>
						<option value="9204-6039">Claro</option>
						<option value="8835-5643">Oi</option>
					</select>
					<span id="telCelular">9975-7859</span>
				</p>
				<p>Ou faca-nos uma visita no ponto A do mapa</p>
				<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=d&amp;source=s_d&amp;saddr=-23.226124,-44.727491&amp;daddr=&amp;hl=en&amp;geocode=&amp;sll=-23.221904,-44.721565&amp;sspn=0.016446,0.028882&amp;mra=mift&amp;mrsp=0&amp;sz=16&amp;ie=UTF8&amp;ll=-23.221904,-44.721565&amp;spn=0.016446,0.028882&amp;t=m&amp;output=embed">
				</iframe>
				<br/>
				<br><br>
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

class Confirmacao(webapp2.RequestHandler):
    def post(self):
    	message = mail.EmailMessage(sender="Davi Trindade <davitrindade@gmail.com>",
                            subject="Casa de Bambu: "+self.request.get('nome')+", de: "+ self.request.get('dataEntrada') +" a: "+ self.request.get('dataSaida'),
							to="fpnsantos@gmail.com",reply_to=" "+self.request.get('nome')+" <"+self.request.get('email')+">",
                            body="Remetente: "+self.request.get('nome')+
							"\nDatas: "+ self.request.get('dataEntrada') +" a: "+ self.request.get('dataSaida') + 
							"\nTelefone: "+self.request.get('tel')+"\nEmail: "+self.request.get('email')+"\nMensagem: \n"+self.request.get('msg'))
	message.send()
	
	self.response.out.write("""

<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
<head>
	<meta charset="UTF-8" content="text/html" />
  	<meta name="description" content="Hospedagem para casais ou grupos na cidade de Paraty em um ambiente cercado de um jardim com especies da mata atlantica em uma casa feita de Bambu. Somos uma familia local e tambem ajudamos com dicas de passeios e muito mais! Otimos precos!" />
  	<meta name="keywords" content="paraty, hospedagem, hotel, pousada, barata, casa, bambu, grupos, passeios, local, carnaval, reveillon, passeio, barco" />

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
			<img src="img/head.jpg" alt="Header Bambu" width="960" height="50" />
			<div class="wifi">
				<img src="img/wifi.gif" width="60" height="24" alt="Disponibilizamos Internet Wi-Fi" />
			</div>
			<div class="opcoes">
				<ul>
				<li><a href="index.html">inicio</a></li>
				<li><a href="casa.html">casa</a></li>
				<li><a href="quartos.html">quartos</a></li>
				<li><a href="faq.html">faq</a></li>
				<li><a href="contato.html">contato</a></li>
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

			<div class="simple-images">
				<p>Obrigado por seu contato! Responderemos a sua consulta em ate 24 horas.</p>
				<p>
				Entre em contato conosco por telefone (DDD 24):
				</p>
				<p>
					3371-0365 Fixo | 9975-7859 Vivo | 8130-2503 TIM |
					9204-6039 Claro | 8835-5643 OI
				</p>
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
			<img src="img/foot.jpg" alt="Footer Bambu" width="480" height="50"><img src="img/foot.jpg" alt="Footer Casa de Bambu" width="480" height="50">
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