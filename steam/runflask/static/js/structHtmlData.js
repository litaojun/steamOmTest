//计划选择框，select数据构造
function structurePlanTimeData(id,plantime)
{
                var itemstr =  "<option value=\"" + id + "\">" + plantime + "</option>";
                return itemstr

            }
//根据接口用例执行成功，失败，ERROR统计汇总
function structureInterfaceTotal(interfaceName,total,success,fail,error,index)
{
                ifccls = "passClass";
                if(fail > 0)
                    ifccls = "failClass";
                if(error > 0)
                    ifccls = "errorClass";
                var data =     "<tr class='" + ifccls + "'>"    +
                               "<td>" + interfaceName + "</td>" +
                               "<td>" + total         + "</td>" +
                               "<td>" + success       + "</td>" +
                               "<td>" + fail          + "</td>" +
                               "<td>" + error         + "</td>" +
                               "<td><a href=\"javascript:showClassDetail('c" + index + "'," + total + ")\">Detail</a></td>" +
                               "<td>--</td>"  +
                               "</tr>";
                return data


            }
//构造用例数据行
function structureTestCaseData(resultSign,i,index,testcaseid,testpoint,errordes,interfaceName,methodName)
{
                 var signdetail = "pass";
                 var trid = "pt";
                 var cls = "None";
                 var hcls ="hiddenRow";
                 if(resultSign == "1")
                 {
                        signdetail = "error";
                        trid = "ft";
                        cls = "failCase";
                }
                if(resultSign == "2")
                {
                        signdetail = "fail";
                        trid = "ft";
                        cls = "errorCase";
                }
               var testcasestr = "<tr id='"+ trid + index + "." + (i+1) + "' class='" + hcls + "' interface='" + interfaceName + "' caseId='" + testcaseid + "' method='" + methodName  +"'>" +
                                     "<td class='"  + cls + "' interface='" + interfaceName + "' caseId='" + testcaseid   +"'><div class='testcase'>" + testcaseid + "_" + testpoint + "</div></td>" +
                                     "<td colspan='5' align='center'>" +
                                           "<a class=\"popup_link\" onfocus='this.blur();' href=\"javascript:showTestDetail('div_"+ trid + index + "." + (i+1) + "')\" >" + signdetail + "</a>" +
                                           "<div id='div_"+trid+ index + "." + (i+1) +"' class=\"popup_window\">" +
                                           "<div style='text-align: right; color:red;cursor:pointer'>" +
                                           "<a onfocus='this.blur();' onclick=\"document.getElementById('div_"+trid+ index + "." + (i+1) +"').style.display = 'none' \" >" +
                                           "[x]</a>" +
                                           "</div>"  +
                                           "<pre>"   + errordes + "</pre>" +
                                           "</div>"  +
                                        "</td>"      +
                                         "<td><button trid='"+ trid + index +"' name='onecase_" + i + "_" + testcaseid + "' type='button' interfaceName='"+ interfaceName +"' caseId='" + testcaseid + "'  >run</button></td>" +
                                     "</tr>";
               return testcasestr;
            }
//所有用例执行情况汇总
function structureBtTotal(casetotal,casesuccess,casefail,caseerror)
{
                totalstr = "<tr id='total_row'>"	+
                                "<td>Total</td>"  +
                                "<td>" + casetotal +  "</td>"  +
                                "<td>" + casesuccess + "</td>"  +
                                "<td>" + casefail    + "</td>"   +
                                "<td>" + caseerror   + "</td>"  +
                                "<td>&nbsp;</td>"    +
                             "</tr>";
                return totalstr;
            }

//获取接口列表，生成行HTML
function structureInterfaceData(aliasName,interfaceAddr,reqtype,module,mark,reqpath,rsppath)
{
                       interfaceData =  "<tr class='interfaceClass'>"       +
                                          "<td>" + aliasName + "</td>"          +
                                          "<td>" + interfaceAddr + "</td>"      +
                                          "<td>" + reqtype + "</td>"      +
                                          "<td>" + module  + "</td>"            +
                                          "<td>" + mark    + "</td>"            +
                                          "<td>" + reqpath + "</td>"            +
                                          "<td>" + rsppath + "</td>"            +
                                          "</tr>";
                       return interfaceData;
                    }