//updating cel phone operator details
$(function() {
		$( "#telefones" ).change(function() {
			$( "#telCelular" ).text( $( this ).val() );
		});
	});

// loading jquery datepicker 
$(function() {
	$( "#dataSaida" ).datepicker({ 
		dateFormat: 'd M yy',
		dayNames: ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado'],
		dayNamesMin: ['D','S','T','Q','Q','S','S','D'],
		monthNames: ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
		prevText: '&#x3c;Anterior',
		nextText: 'Seguinte',
		monthNamesShort: ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
		/*dayNamesShort: ['Dom','Seg','Ter','Qua','Qui','Sex','Sáb','Dom'],*/
	});
    
    $( "#dataEntrada" ).datepicker({
		dateFormat: 'd M yy',
		dayNames: ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado'],
		dayNamesMin: ['D','S','T','Q','Q','S','S','D'],
		monthNames: ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
		monthNamesShort: ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'],
		prevText: '&#x3c;Anterior',
		nextText: 'Seguinte',
		minDate: 0,
		onSelect: function(dateText, inst) { 
			var date = $('#dataEntrada').datepicker('getDate');
			if (date) {	
				date.setDate(date.getDate() + 1);
				$('#dataSaida').datepicker('option', 'minDate', date);
			}
			$('#dataSaida').datepicker('show');
			$('#dataSaida').datepicker('select');
		}
	});
	
	
});

// handle the form submit event
function prepareEventHandlers(errorMessage) {
	document.getElementById("frmContact").onsubmit = function() {
		// prevent a form from submitting if no email.
		if ( (document.getElementById("email").value == "") ||
		 	 (document.getElementById("dataEntrada").value == "") ||
			 (document.getElementById("dataSaida").value == "") 
			) {
			document.getElementById("errorMessage").innerHTML = errorMessage;
			// to STOP the form from submitting
			return false;
		} else {
			// reset and allow the form to submit
			document.getElementById("errorMessage").innerHTML = "";
			return true;
		}
	};
}
