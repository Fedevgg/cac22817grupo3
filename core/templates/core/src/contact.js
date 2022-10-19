'use strict'

window.addEventListener('load', function(){
	let formulario = document.querySelector('form');


	formulario.addEventListener('submit', ()=>{
   
		console.log("Evento submit capturado");

		let nombre = document.querySelector("#nombre").value;
		let apellidos = document.querySelector("#apellido").value;
		let edad = parseInt(document.querySelector("#edad").value);
        let email= document.querySelector('#email').value;
        let err= document.querySelector('.err');
        

		if(nombre.trim() == null || nombre.trim().length == 0){
            err.style.display="flex";
			err.innerHTML = "El nombre no puede estar vacio";
			return false;
		}

		if(apellidos.trim() == null || apellidos.trim().length == 0){
            err.style.display="flex";
			err.innerHTML = "El apellido no puede estar vacio";
			return false;
		}

		if(edad == null || edad <= 0 || isNaN(edad)){
            err.style.display="flex";
			err.innerHTML = "La edad debe ser mayor a 0";
			return false;
		}

        if(email==null || email.trim().length == 0){
            err.style.display="flex";
            err.innerHTML = "El email no puede estar vacio";
			return false;
        }
		err.style.display="none";
        document.querySelector('.fondo_transparente').style.display="block";

	});

    document.querySelector('#close_modal').addEventListener('click',()=>{
        document.querySelector('.fondo_transparente').style.display="none";
    });

    
});