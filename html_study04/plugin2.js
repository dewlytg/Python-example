/**
 * Created by alex on 2016/11/26.
 */

// 匿名函数防止扩展中的变量和函数名冲突
(function (arg) {

    var status = 1;

    arg.extend({
       'wangsen': function () {
           return 'sb';
       }
    });

})(jQuery);
