/** First Slider */
$('.slider-one')
.not(".slick-initialized")
.slick({
    autoplay: true,
    autoplaySpeed: 3000,
    dots: true,
    prevArrow: ".prev",
    nextArrow: ".next",
});

/** Second Slider */
$('.slider-two')
.not(".slick-initialized")
.slick({
    prevArrow: "site-slider-two.prev",
    nextArrow: "site-slider-two.next",
    slidesToShow: 5,
    slidesToScroll:1,
    autoplaySpeed: 3000,
});


