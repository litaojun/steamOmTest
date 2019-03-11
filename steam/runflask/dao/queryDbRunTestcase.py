from steam.runflask.dao.queryDbFlask import getDbManger
def queryTokenByPlanId(planId = None,projectName = None):
    updateProcessSql = "update test_run_process set status=1 where projectname = '%s' and planId = '%s';" % (projectName, planId)
    querySql         = "select p.token from test_run_process p where p.planId = %d and p.projectname = '%s';" % (planId,projectName)
    dbManager        = getDbManger()
    dbManager.updateData(sql=updateProcessSql,dbName="ltjtest")
    rstData          = dbManager.queryAll(sql = querySql,dbName="ltjtest")
    return rstData[0][0]
