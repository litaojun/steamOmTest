var hostIp = "http://127.0.0.1:8181";
function getTestCaseDetail()
{
        interfaceName = $(this).attr("interface").substr(28);
        caseId   =  $(this).attr("caseid");
        planId       = $("#select_plan").val();
	    runprocessurl = ipStr + "/rptqy/prop/getOneTestcase?interface="+interfaceName+ "&caseId="+caseId+"&planId=" + planId;
		$.ajax({
				   type:"GET",
				   url: runprocessurl,
				   dataType:"json",
				   success: function(data){
				                           $("#result_table").attr("class","hiddenRow");
                                           $("#casetable").attr("class","");
				                           $("#buttontab").attr("class","");
				                             var reg = new RegExp("\n", "g");//g,表示全部替换
				                             $("input[name='caseid']").attr("value" , data[0]);
											 $("input[name='interface']").attr("value" , data[1]);
											 $("input[name='testpoint']").attr("value" , data[2]);
											 $("td[name='pretestrun']").html( data[3].replace(reg, "<br>"));
											 $("td[name='operatorMethod']").html(data[4].replace(reg, "<br>"));
											 $("td[name='testdata']").html( data[5].replace(reg, "<br>"));
											 $("td[name='expentresult']").html( data[6].replace(reg, "<br>"));
											 $("td[name='casepathtxt']").html( data[8]);
											 $("td[name='testclasstxt']").html(data[9]);
											 $("td[name='caseidtxt']").html( data[0]);
											 $("td[name='interfacetxt']").html( data[1]);
											 $("td[name='testpointtxt']").html(data[2]);
											 if( data[10] == 0 )
											       $("td[name='result']").html("fail");
                                             if( data[10] == 1 )
											       $("td[name='result']").html("sucess");
				                          }
				});
}

function updateRunTestCaseResult()
{
        interfaceName = $("td[name='interfacetxt']").html();
        caseId   =  $("td[name='caseidtxt']").html();
        planId       = $("#select_plan").val();
	    runprocessurl = hostIp + "/rptqy/prop/getOneTestcase?interface="+interfaceName+ "&caseId="+caseId+"&planId=" + planId;
		$.ajax({
				   type:"GET",
				   url: runprocessurl,
				   dataType:"json",
				   success: function(data){
											 if( data[10] == 0 )
											       $("td[name='result']").html("fail");
                                             if( data[10] == 1 )
											       $("td[name='result']").html("sucess");
				                          }
				});
}