; (function ($) {
    "use strict"


    var nav_offset_top = $('header').height() + 50;
    /*-------------------------------------------------------------------------------
	  Navbar 
	-------------------------------------------------------------------------------*/

    //* Navbar Fixed  
    function navbarFixed() {
        if ($('.header_area').length) {
            $(window).scroll(function () {
                var scroll = $(window).scrollTop();
                if (scroll >= nav_offset_top) {
                    $(".header_area").addClass("navbar_fixed");
                } else {
                    $(".header_area").removeClass("navbar_fixed");
                }
            });
        };
    };
    navbarFixed();

    // Search Toggle
    $("#search_input_box").hide();
    $("#search").on("click", function () {
        $("#search_input_box").slideToggle('slow');
        $("#search_input").focus();
    });
    $("#close_search").on("click", function () {
        $('#search_input_box').slideUp('slow');
    });


    /*----------------------------------------------------*/
    /*  Clients Slider
    /*----------------------------------------------------*/
    function active_testimonial() {
        if ($('.active_testimonial').length) {
            $('.active_testimonial').owlCarousel({
                loop: true,
                margin: 0,
                items: 1,
                nav: false,
                autoplay: false,
                smartSpeed: 1500,
                dots: false,
                responsiveClass: true,
                thumbs: true,
                thumbsPrerendered: true,
            })
        }
    }
    active_testimonial();


    /*----------------------------------------------------*/
    /*  MailChimp Slider
    /*----------------------------------------------------*/
    function mailChimp() {
        $('#mc_embed_signup').find('form').ajaxChimp();
    }
    mailChimp();

    $('select').niceSelect();

    /*----------------------------------------------------*/
    /*  Simple Counter js
    /*----------------------------------------------------*/
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });

    /*----------------------------------------------------*/
    /*  Google map js
    /*----------------------------------------------------*/

    if ($('#mapBox').length) {
        var $lat = $('#mapBox').data('lat');
        var $lon = $('#mapBox').data('lon');
        var $zoom = $('#mapBox').data('zoom');
        var $marker = $('#mapBox').data('marker');
        var $info = $('#mapBox').data('info');
        var $markerLat = $('#mapBox').data('mlat');
        var $markerLon = $('#mapBox').data('mlon');
        var map = new GMaps({
            el: '#mapBox',
            lat: $lat,
            lng: $lon,
            scrollwheel: false,
            scaleControl: true,
            streetViewControl: false,
            panControl: true,
            disableDoubleClickZoom: true,
            mapTypeControl: false,
            zoom: $zoom,
            styles: [
                {
                    "featureType": "water",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#dcdfe6"
                        }
                    ]
                },
                {
                    "featureType": "transit",
                    "stylers": [
                        {
                            "color": "#808080"
                        },
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#dcdfe6"
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        }
                    ]
                },
                {
                    "featureType": "road.local",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#ffffff"
                        },
                        {
                            "weight": 1.8
                        }
                    ]
                },
                {
                    "featureType": "road.local",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#d7d7d7"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#ebebeb"
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#a7a7a7"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        }
                    ]
                },
                {
                    "featureType": "landscape",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#efefef"
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "color": "#696969"
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#737373"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "labels",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#d6d6d6"
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {},
                {
                    "featureType": "poi",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#dadada"
                        }
                    ]
                }
            ]
        });
    }

    /*----------------------------------------------------*/
    /*  Google map js
    /*----------------------------------------------------*/

    if ($('#mapBox2').length) {
        var $lat = $('#mapBox2').data('lat');
        var $lon = $('#mapBox2').data('lon');
        var $zoom = $('#mapBox2').data('zoom');
        var $marker = $('#mapBox2').data('marker');
        var $info = $('#mapBox2').data('info');
        var $markerLat = $('#mapBox2').data('mlat');
        var $markerLon = $('#mapBox2').data('mlon');
        var map = new GMaps({
            el: '#mapBox2',
            lat: $lat,
            lng: $lon,
            scrollwheel: false,
            scaleControl: true,
            streetViewControl: false,
            panControl: true,
            disableDoubleClickZoom: true,
            mapTypeControl: false,
            zoom: $zoom,
            styles: [
                {
                    "featureType": "administrative.country",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "visibility": "simplified"
                        },
                        {
                            "hue": "#ff0000"
                        }
                    ]
                }
            ]
        });
    }


})(jQuery)

// custom Javascript
let resoPopUpCloseBtn = document.getElementById('reso_close_btn')
let resoPopUpCloseDiv = document.getElementById('reso_close')


resoPopUpCloseBtn.addEventListener('click', (e) => {
 
    resoPopUpCloseDiv.classList.remove('dis-blk')
    resoPopUpCloseDiv.classList.add('dis-none')

});


const accessProgram = (id = NaN, code) => {
    console.log('Requesting access with passcode!')
    console.log(id)
    let accessBtn = document.getElementsByClassName('program_class_btn')[0]
    let errorCard = document.getElementsByClassName('error-card-program')[0]
    let resourceWrapper = document.getElementsByClassName('reso-inner-wrapper')[0]

    $.ajax({
        type: 'POST',
        url: `http://127.0.0.1:8000/programs/view/course-passcode-validate/?id=${id}&code=${code}`,

        beforeSend: () => {
            accessBtn.innerHTML = 'Checking...'
            accessBtn.disabled = true;
        },
        complete: () => {
            accessBtn.innerHTML = 'Access Classroom'
            accessBtn.disabled = false;
        },
        success: (data) => {
            // do something
            console.log(data)
            if (data.code == 200){

                errorCard.innerHTML = `Success &#10003;`
                errorCard.style.background = '#28a745'
                errorCard.classList.remove('in-error-card')
                errorCard.classList.add('out-error-card')

                // wait for 5s
                setTimeout((e) => {
                    errorCard.classList.remove('out-error-card')
                    errorCard.classList.add('in-error-card')
                    resoPopUpCloseDiv.classList.remove('dis-none')
                    resoPopUpCloseDiv.classList.add('dis-blk')

                    // loop through resources and add to list
                    let reso = ''
                    if (data.resource.length < 1){
                        reso = `<div style="background-color: #ee3e4f; display: block; display: block; padding: 20px; border-radius: 5px; color: #fff;" >
                                        This Program Have no Resources Yet! &#10060;
                                    </div>`
                    } else {
                        for (let index = 0; index < data.resource.length; index++) {
                            const element = data.resource[index];
                            if (element.type_of == "video") {
                                reso += `<div class="reso">
                                    <a href="${element.link || element.Document_upload}" target="_blank">
                                        <img src="https://res.cloudinary.com/afmdjango/image/upload/v1672646820/video-marketing_uweost.png" alt="video or audio play icon">
                                        <p>${element.file_title}</p>
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M320 0c-17.7 0-32 14.3-32 32s14.3 32 32 32h82.7L201.4 265.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L448 109.3V192c0 17.7 14.3 32 32 32s32-14.3 32-32V32c0-17.7-14.3-32-32-32H320zM80 32C35.8 32 0 67.8 0 112V432c0 44.2 35.8 80 80 80H400c44.2 0 80-35.8 80-80V320c0-17.7-14.3-32-32-32s-32 14.3-32 32V432c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16V112c0-8.8 7.2-16 16-16H192c17.7 0 32-14.3 32-32s-14.3-32-32-32H80z"/></svg>

                                    </a>
                                </div>`
                            } else {
                                reso += `<div class="reso">
                                    <a href="${element.link || element.Document_upload}" download="">
                                        <img src="https://res.cloudinary.com/afmdjango/image/upload/v1672646820/document-icon_t5eiof.png" alt="file icon">
                                        <p>${element.file_title}</p>
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M288 32c0-17.7-14.3-32-32-32s-32 14.3-32 32V274.7l-73.4-73.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l128 128c12.5 12.5 32.8 12.5 45.3 0l128-128c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L288 274.7V32zM64 352c-35.3 0-64 28.7-64 64v32c0 35.3 28.7 64 64 64H448c35.3 0 64-28.7 64-64V416c0-35.3-28.7-64-64-64H346.5l-45.3 45.3c-25 25-65.5 25-90.5 0L165.5 352H64zM432 456c-13.3 0-24-10.7-24-24s10.7-24 24-24s24 10.7 24 24s-10.7 24-24 24z"/></svg>
                                    </a>
                                </div>`
                            }
                            
                    }
                        
                    }

                    resourceWrapper.innerHTML = reso
                }, 2000)

            }
    
        },
        error: (err) => {
            // do something
            if (err.responseJSON) {
                errorCard.innerHTML = `${err.responseJSON.message} &#10060;`
            } else {
                errorCard.innerHTML = `${err.statusText}`
            }
            
            errorCard.style.background = '#ee3e4f'
            console.log('failed', err)
            errorCard.classList.remove('in-error-card')
            errorCard.classList.add('out-error-card')
            // wait for 3s
            setTimeout((e) => {
                errorCard.classList.remove('out-error-card')
                errorCard.classList.add('in-error-card')
            }, 5000)

            accessBtn.innerHTML = 'Access Classroom'
            accessBtn.disabled = false;
        },
    });



};

let programAccessForm = document.getElementById('programAccessForm')
let programAccessInput = document.getElementById('programAccessInput')
let programID = document.getElementById('programID')

programAccessForm.addEventListener('submit', (e) => {
    e.preventDefault()
    console.log(programID.innerText)
    accessProgram(id = programID.innerText, code = programAccessInput.value);

});

// API Endpont
// http://127.0.0.1:8000/programs/view/course-passcode-validate/?title=Second Coming of Christ 2&code=OknIarns4QkBvqTggQUO


