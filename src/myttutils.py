import os, subprocess, shlex

def ttut_get_envvar(env, val):
    envval = os.environ.get(env)
    if (envval is None or envval ==""):
        return val
    else:
        if type(val)==type(0):        # int type
            return int(envval)
        elif type(val)==type(0.1):    # float type
            return float(envval)
        elif type(val)==type(True):    # bool type
            return bool(envval)
    return envval

def ttut_extract_value_from_env(envfile, mykey, defval):
  fh = open(envfile, "r")
  lines = fh.readlines()
  fh.close()
  for line in lines:
    if line.find(mykey)==0:
      line_split = line.split(mykey)
      return line_split[1].strip()
  return defval


def ttut_make_dirs(prpath):
  if not os.path.exists(prpath):
    print("making path: %s" % (prpath))
    cmd = "mkdir -p \"%s\"" % (prpath)
    subprocess.call(shlex.split(cmd), shell=False)

def ttut_clone_git(prpath, giturl):
  if not os.path.exists(prpath):
    cmd = "git clone %s %s" % (giturl, prpath)
    subprocess.call(shlex.split(cmd), shell=False)
  else:
    print("repository folder already exist in %s" % (prpath))
    wd=prpath
    cmd = "git pull"
    subprocess.call(shlex.split(cmd), cwd=wd, shell=False)
    cmd = "git status -s"
    subprocess.call(shlex.split(cmd), cwd=wd, shell=False)

def ttut_copy_file_from_to(filename, srcpath, dstpath):
  dstfull=os.path.join(dstpath, filename)
  srcfull=os.path.join(srcpath, filename)
  if not os.path.exists(dstfull):
    if os.path.isfile(srcfull):
      ttut_make_dirs(dstpath)
      subprocess.call(["cp", srcfull , dstfull])
    else:
      print("source file %s does not exist, can not copy!" % (srcfull))
  else:
    print("%s already exist in %s" % (srcfull, dstpath))

def ttut_aifile_dl_to_path(aifile_addr, aifile_cred, fileurl, filename, localpath):
  if not os.path.exists(os.path.join(localpath, filename)):
    full_addr="%s/remote.php/webdav/%s%s" % (aifile_addr, fileurl, filename)
    print("downloading file %s to %s" % (full_addr, localpath))
    ttut_make_dirs(localpath)
    subprocess.call([
                "curl",
                "-u", aifile_cred,
                full_addr,
                "-OJLs"
                ], cwd=localpath, shell=False)
