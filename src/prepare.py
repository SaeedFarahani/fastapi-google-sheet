import os, subprocess
import myttutils as ttut

AIFILE_ADDR=ttut.ttut_get_envvar("AIFILE_ADDR", "https://aifile.tosantechno.com")
AIFILE_CRED=ttut.ttut_get_envvar("AIFILE_CRED", "Uploader:SalamUpload@1399")
CUS_DATA=ttut.ttut_get_envvar("VOLUME_DIR_CUS_DATA", "./data")
SERVICENAME=ttut.ttut_get_envvar("SERVICENAME", "ASSIGNMENTapi")
# datapath='%s' % (CUS_DATA)

# dirs = ['logs'] + (['database'] if ttut.ttut_get_envvar("TARGET_DEPLOY_TYPE", '')=='dev'  else [])
# for dname in dirs:
#   ttut.ttut_make_dirs(os.path.join(datapath, SERVICENAME, 'data', dname))

DC_SERVICE_NAME = ttut.ttut_get_envvar('DC_SERVICE_NAME', 'assingmentapi')
VOLUME_DIR_APP_DATA = ttut.ttut_get_envvar('VOLUME_DIR_APP_DATA', '../app_data')
VOLUME_DIR_CUS_DATA = ttut.ttut_get_envvar('VOLUME_DIR_CUS_DATA', '../cus_data')

cuspath = os.path.join(VOLUME_DIR_CUS_DATA, DC_SERVICE_NAME, 'data')
# apppath = os.path.join(VOLUME_DIR_APP_DATA, DC_SERVICE_NAME, 'data')

dirs = ['database', 'logs']
for dname in dirs:
    ttut.ttut_make_dirs(os.path.join(cuspath, dname))

savedir = 'assingmentapi/data/servicetests'
ttut.ttut_make_dirs(os.path.join(VOLUME_DIR_APP_DATA, savedir))


fileurl = 'assingmentapi/'
savepath = os.path.join(VOLUME_DIR_APP_DATA, savedir)

filename_list = ['params.pkl', 'train_catvnoncat.h5', 'test_catvnoncat.h5']
for filename in filename_list:
  ttut.ttut_aifile_dl_to_path(aifile_addr=AIFILE_ADDR, aifile_cred=AIFILE_CRED,
                            fileurl=fileurl, filename=filename, localpath=savepath)