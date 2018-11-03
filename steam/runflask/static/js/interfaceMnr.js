//获取选择项目的所有接口列表
function getInterfaceListData()
{
                            $.ajax({
                                       type:"GET",
                                       url : ipStr + "/infcs/prop/interfacelist?projectname=steam亲子教育" ,
                                       dataType :"json" ,
                                       success: function(data)
                                       {
                                           $("#result_table").attr("class","hiddenRow");
                                           $("#interface_table").attr("class","");
                                           $("tr[class='interfaceClass']").remove();
                                           $.each(data.infsList,function(index,item)
                                           {
                                                  trData = structureInterfaceData(item.aliasName,
                                                                                   item.interfaceAddr,
                                                                                   item.reqtype,
                                                                                   item.module,
                                                                                   item.mark,
                                                                                   item.reqpath,
                                                                                   item.rsppath);
                                                  $("#interface_table").append(trData);
                                           });
                                       }
                                    });
                     }

