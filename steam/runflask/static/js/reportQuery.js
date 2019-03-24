// ipStr = "http://127.0.0.1:8181";
// ipStr = "http://10.205.255.241:8181";
// testReporturl = ipStr + "/rptqy/prop/testappmap?planid=";   //#根据选择的执行计划获取对应报告
// runTesturl   = ipStr + "/prop/runtestplan?projectname=";  //根据项目名称执行自动化测试
function getAllPlanByProName()
{
         $("#result_table").attr("class", "");
         $("#interface_table").attr("class", "hiddenRow");
         projectname = $("#select_project").find("option:selected").text();
         selectPlanByProName(projectname);
        clearTestStatusAndTime();
}
//根据项目名称获取所有的计划
function selectPlanByProName(proname)
{
    $.ajax({
              type:"GET",
              url: ipStr + "/rptqy/prop/testplanlist?projectname=" + proname ,
              dataType:"json",
              <!--global:false,-->
              success: function(data){
                                       clearTestReportTable();
                                       clearPlanTimeList();
                                       var sign = '';
                                       $.each(data.listplan,function(index,item){
                                               var itemstr = structurePlanTimeData(item.id,item.plantime);
                                               $("#select_plan").prepend(itemstr);
                                               sign = item.id;
                                             }
                                             );
                                     $("#select_plan").prepend("<option value='' selected>--计划--</option>") ;
                                     $("#select_plan").find("option[value='"+sign+"']").attr("selected",true);   //选中第一行数据
                                     $('#select_plan').trigger('change');//触发改变事件
              }

			});
		   }

//根据选择的执行计划时间获取对应测试报告
function selectfun(event)
{
         testReporturl = ipStr + "/rptqy/prop/testappmap?planid=";
		 $("#result_table").attr("class","");
         $("#interface_table").attr("class","hiddenRow");
		 lid = $(this).val()  ;//获取选中计划的planId
		 $.ajax({
		         type :"GET" ,
                 url : testReporturl + lid ,
                 dataType :"json" ,
                 <!--global:false,-->
		         success: function(data){
                                          clearTestReportTable();
                                          listdata = data.testrst	;
                                          casetotal = 0;
                                          casesuccess = 0;
                                          casefail = 0;
                                          caseerror = 0;
									      $.each(listdata,function(index,item)
                                                  {
                                                        casetotal   = casetotal    + item.total;
                                                        casesuccess = casesuccess  + item.success;
                                                        casefail    = casefail     + item.fail;
                                                        caseerror   = caseerror    + item.error;
                                                        var addr = structureInterfaceTotal(item.interfaceName,item.total,item.success,item.fail,item.error,index);
                                                        $("#result_table").append(addr);
                                                        $.each(item.result,function(i,tcase)
                                                                {
                                                                  testcasestr = structureTestCaseData(tcase.resultSign,i,index,tcase.testcaseid,tcase.testpoint,tcase.errordes,item.interfaceName);
                                                                  $("#result_table").append(testcasestr);
                                                                }
                                                               );
                                                  });
												  $("button[name^='onecase']").bind("click",runOneTestcae);
												      //$("tr[id^='ft'],tr[id^='pt']").bind("click",getTestCaseDetail);
												      //$(".errorCase, .failCase,td[class='None']").bind("click",getTestCaseDetail);
                                                  totalstr = structureBtTotal(casetotal,casesuccess,casefail,caseerror);
                                                  $("#result_table").append(totalstr);
                                           }
								   });
}

//根据选择的执行计划时间获取对应测试报告
function queryReportByPlanId(planId,trid)
{
			      $("#result_table").attr("class","");
                  $("#interface_table").attr("class","hiddenRow");
				  $.ajax({
					       type :"GET" ,
                            url : testReporturl + planId ,
                           dataType :"json" ,
                           <!--global:false,-->
					        success: function(data){
                                                      clearTestReportTable();
                                                      listdata = data.testrst	;
                                                      casetotal = 0;
                                                      casesuccess = 0;
                                                      casefail = 0;
                                                      caseerror = 0;
												      $.each(listdata,function(index,item)
                                                      {
														        casetotal   = casetotal    + item.total;
														        casesuccess = casesuccess  + item.success;
															    casefail    = casefail     + item.fail;
															    caseerror   = caseerror    + item.error;
                                                                var addr = structureInterfaceTotal(item.interfaceName,item.total,item.success,item.fail,item.error,index);
																$("#result_table").append(addr);
                                                                $.each(item.result,function(i,tcase){
                                                                                                        testcasestr = structureTestCaseData(tcase.resultSign,i,index,tcase.testcaseid,tcase.testpoint,tcase.errordes,item.interfaceName);
                                                                                                        $("#result_table").append(testcasestr);
                                                                                                      }
                                                                      );
                                                      });
												      $("button[name^='onecase']").bind("click",runOneTestcae);
												      // $("tr[id^='ft'],tr[id^='pt']").bind("click",getTestCaseDetail);
                                                      $(".errorCase,.failCase,td[class='None']").bind("click",getTestCaseDetail);
                                                      totalstr = structureBtTotal(casetotal,casesuccess,casefail,caseerror);
                                                      $("#result_table").append(totalstr);
                                                      $("tr[id^='"+trid+"']").attr("class","None");
                                                    }
								   });
}

function clearTestStatusAndTime()
{
		 $("#timePlan").html("-------");
		 $("#statusPlan").html("----");
		 $("#fentime").html("-");
		 $("#miaotime").html("-");
}

function clearTestReportTable()
{
                $("tr[class='errorClass'],tr[class='failClass'],tr[class='passClass']").remove();
                $("tr[id^='ft'],tr[id^='pt']").remove();
                $("#total_row").remove();
}

function  clearPlanTimeList()
{
                 $("#select_plan > option").remove();
}

function clearAllContent()
{
                      $("tr[class='errorClass'],tr[class='failClass'],tr[class='passClass']").remove();
                      $("tr[id^='ft'],tr[id^='pt']").remove();
                      $("#total_row").remove();
                      $("#select_plan > option").remove();
                      $("#select_plan").prepend("<option value='' selected>--计划--</option>") ;
}


function bingEvent()
{
         $("button[name^='onecase']").bind("click",runOneTestcae);       //
         $("#planTest").bind("click",autoTestFun);                        //点击自动接口测试
         $("#select_plan").bind("change",selectfun);                      //选择一个执行计划
         $("#interfaceMngr").bind("click",getInterfaceListData);          //接口管理
         $('body').everyTime('30s',timeTest);                              //定时检查是否执行完成
         $("#select_project").bind("change",getAllPlanByProName);	       //选择一个项目
         $("tr[id^='ft'],tr[id^='pt']").bind("click",getTestCaseDetail); //
         $("#rtnHome").bind("click",retuntHome);	                        //选择一个项目
         $("#runOneCaseDetail").bind("click",runOneTestcae);              //

}

function retuntHome()
{
       $("#result_table").attr("class","");
       $("#casetable").attr("class","hiddenRow");
       $("#buttontab").attr("class","hiddenRow");
}

