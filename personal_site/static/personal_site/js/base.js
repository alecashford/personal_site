jQuery(function ($) {
    var $bodyEl = $('body'),
        $sidedrawerEl = $('#sidedrawer');

    function hideSidedrawerContents() {
        $bodyEl.toggleClass('hide-sidedrawer');
    }

    $('#sidegrip').on('click', hideSidedrawerContents);

    var $titleEls = $('strong', $sidedrawerEl);
    
    $titleEls
        .next()
        .hide();
    
    $titleEls.on('click', function () {
        $(this).next().slideToggle(200);
    });
});
