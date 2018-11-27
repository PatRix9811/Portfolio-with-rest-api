function print_message()
{
   var title = document.getElementById('id_title').value;
   var email = document.getElementById('id_email').value;
   var message = document.getElementById("id_message").value;

   if(title.length>0 && email.length >0 && message.length >0)
   {
      document.getElementById("message").innerHTML = 'Message was send';
   }

}