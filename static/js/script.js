$flag = -1;
$(".day").hover(
    function () {
        $(".popup", this).attr("style", "display:block");
    },
    function () {
        if ($flag == -1) {
            $(".popup", this).attr("style", "display:none");
        }
    }
);

$(".popup").click(function () {
    $('this').attr("style", "display:block");
});