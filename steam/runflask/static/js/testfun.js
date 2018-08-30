( function ($){
			$.fn.serializeJson= function ()
			{
				var serializeObj={};
				var array= this .serializeArray();
				var str= this .serialize();
				$(array).each( function (){
				if (serializeObj[ this .name]){
				if ($.isArray(serializeObj[ this .name])){
				serializeObj[ this .name].push( this .value);
				} else {
				serializeObj[ this .name]=[serializeObj[ this .name], this .value];
				}
				} else {
				serializeObj[ this .name]= this .value;
				}
				});
				return serializeObj;
			};
			})(jQuery);
			 
			(function($){ 
			    $.fn.serializeJson=function(){ 
			      var serializeObj={}; 
			      var array=this.serializeArray(); 
			      var str=this.serialize(); 
			      $(array).each(function(){ 
			        if(serializeObj[this.name]){ 
			          if($.isArray(serializeObj[this.name])){ 
			            serializeObj[this.name].push(this.value); 
			          }else{ 
			            serializeObj[this.name]=[serializeObj[this.name],this.value]; 
			          } 
			        }else{ 
			          serializeObj[this.name]=this.value;  
			        } 
			      }); 
			      return serializeObj; 
			    }; 
			  })(jQuery); 
    /*添加行数据*/
     function GetQueryString(name) {
            var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
            var r = window.location.search.substr(1).match(reg);  //获取url中"?"符后的字符串并正则匹配
            var context = "";
            if (r != null)
                 context = r[2];
            reg = null;
            r = null;
            return context == null || context == "" || context == "undefined" ? "" : context;
        }