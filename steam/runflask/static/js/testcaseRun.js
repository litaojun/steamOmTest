//运行一个指定的用例
function runOneTestcae()
{
                        projectname     = $("#select_project").find("option:selected").text();
                        planId           = $("#select_plan").find("option:selected").val();
                        projectname     = "steam亲子教育";
                        caseListclass   = $("#result_table").attr("class");
                        caseDetailclass = $("#casetable").attr("class");
                        if(caseListclass == "")
                        {
                            interfaceName = $(this).attr("interfaceName").substr(28);
                            caseId         = $(this).attr("caseId");
                        }
                         if(caseDetailclass == "")
                         {
                            interfaceName = $("td[name='interfacetxt']").html();
                            caseId   =  $("td[name='caseidtxt']").html();
                         }
                         $.ajax({
                                       type:"GET",
                                       url : ipStr + "/tsrun/prop/interfacelist?planId=" + planId + "&projectname=" + projectname + "&interfaceName=" + interfaceName + "&caseId=" + caseId ,
                                       dataType :"json" ,
                                       success: function(data)
                                       {
                                           if(data.code == "000000")
                                           {
                                                // $('#select_plan').trigger('change');
                                                 alert("执行成功");
                                                // $("tr[id^='"+trid+"']").attr("class","None");
                                               if(caseListclass == "")
                                               {
                                                    trid   = $(this).attr("trid");
                                                    queryReportByPlanId(planId,trid);
                                               }
                                               if(caseDetailclass == "")
                                                    updateRunTestCaseResult();


                                           }
                                           else
                                               alert("执行失败");
                                       },
                                       fail:function (data) {
                                           alert("执行失败");
                                       }
                                 });
}

sign = 1;
//定时查询用例执行状态
function timeTest()
{
				     if(sign==0)
                     {
				    	    starttime = $("#timePlan").html();
				    	    runprocessurl =  ipStr + "/tsrun/prop/queryRunProcess?projectname=steam亲子教育"  + "&token=" + tokenId;
						    $.ajax({
										type:"GET",
										url: runprocessurl,
									    dataType:"json",
										<!--global:false,-->
										success: function(data){
										                           if(data.status == 2)
                                                                   {
										                         	    $("#statusPlan").html("自动化用例执行完成");
										                         	    sign =1;
										                         	    protime = data.starttime + "~" + data.endtime;
										                        	    $("#fentime").html(data.mintime);
										                        	    $("#miaotime").html(data.sectime);
										                        	    $("#timePlan").html(protime);
										                        	    selectPlanByProName("steam亲子教育");
										                           }
										                       }
                                     });
                     }
}

//根据选择的项目名称执行自动化测试
function autoTestFun()
{
    projectname = $("#select_project").find("option:selected").text();  //获取select的选择的文本,获取工程名称
    requrl = ipStr + "/tsrun/prop/runTestPro?projectname=" + projectname ; //+ "&startime=" + time2;
    $.ajax({
              type:"GET" ,
              url: requrl ,
              dataType:"json" ,
              <!--global:false,-->
              success: function(data){
                            tokenId = data.token;
                            resfPageFromRuntest(data.starttime);
                            }
              });
}


function resfPageFromRuntest(starttime)
{
        $("#timePlan").html(starttime);
        sign = 0;
	    $("#statusPlan").html("自动化用例执行中，请等待...");
}