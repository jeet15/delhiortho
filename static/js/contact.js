$(document).ready(function(){
    (function($) {
        "use strict";

    
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value)
    }, "type the correct answer -_-");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                subject: {
                    required: true,
                    minlength: 4
                },
                number: {
                    required: true,
                    minlength: 5
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true,
                    minlength: 20
                }
            },
            messages: {
                name: {
                    required: "come on, you have a name, don't you?",
                    minlength: "your name must consist of at least 2 characters"
                },
                subject: {
                    required: "come on, you have a subject, don't you?",
                    minlength: "your subject must consist of at least 4 characters"
                },
                number: {
                    required: "come on, you have a number, don't you?",
                    minlength: "your Number must consist of at least 5 characters"
                },
                email: {
                    required: "no email, no message"
                },
                message: {
                    required: "um...yea, you have to write something to send this form.",
                    minlength: "thats all? really?"
                }
            },
            submitHandler: function(form) {
                $(form).ajaxSubmit({
                    type:"POST",
                    data: $(form).serialize(),
                    url:"contact_process.php",
                    success: function() {
                        $('#contactForm :input').attr('disabled', 'disabled');
                        $('#contactForm').fadeTo( "slow", 1, function() {
                            $(this).find(':input').attr('disabled', 'disabled');
                            $(this).find('label').css('cursor','default');
                            $('#success').fadeIn()
                            $('.modal').modal('hide');
		                	$('#success').modal('show');
                        })
                    },
                    error: function() {
                        $('#contactForm').fadeTo( "slow", 1, function() {
                            $('#error').fadeIn()
                            $('.modal').modal('hide');
		                	$('#error').modal('show');
                        })
                    }
                })
            }
        })
    })
        
 })(jQuery)

        $("select.membertype").change(function(){

        var selectType = $(this).children("option:selected").val();
            if (selectType == 'associate') {
                $(".memberfees").val('1500');
                
            }
            if (selectType == 'lifetime') {
            
                $(".memberfees").val('3000');
                
            }
        });

        $("form[name='registration']").validate({
            rules:{
                membertype:"required",
                firstname:"required",
                email:{
                    required:true,
                    email:true
                },
                password:{
                    required:true
                },
                re_password:{
                    required:true,
                    equalTo: ".password"

                },
                permanent_address:"required",
                mobile:{
                    required:true,
                    number:true,
                    minlength:10,
                    maxlength:10
                }
            },
            messages: {
                membertype:"Please select member type",
                firstname:"Please insert your fullname",
                email:{
                    required:"Please insert the email",
                    email:"Please insert the valid email"
                },
                password:{
                    required:"Please Enter the password"
                },
                re_password:{
                    required:"Please Re-Enter Password",
                    equalTo: "Both the password should be same"

                },
                permanent_address:"Please insert your permanent address",
                mobile:{
                    required:"Please insert a valid mobile number",
                    number:"Only Numbers allowed",
                    minlength:"invalid mobile number",
                    maxlength:"invalid mobile number"
                }
            }

        });

    $(".journal").click(function(){
        alert("This feature is under process !");
    });

    $(".quiz").click(function(){
        alert("This feature is under process !");
    });

})