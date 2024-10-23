import os
import sys
import yaml
import re
#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------
SOFTWARE_DIR='software'
SOFTWARE_MAIN='software-docs'
SOFTWARE_DOCS=SOFTWARE_MAIN+'/docs'
CLUSTERS={
  'cpe23.12' : 'Dardel',
  'cpe23.12.gpu' : 'Dardel-GPU',
  'cpe23.03' : 'Dardel',
  'cpe23.03.gpu' : 'Dardel-GPU',
  }
OLD_CLUSTERS={
  }
#-------------------------------------------------------------------------------
# get files and folder names of folder dirpath
def getDirectoryList(dirpath,mask):
  files=[]
  dirs=[]
  for file in os.listdir(dirpath):
    if os.path.isdir(os.path.join(dirpath, file)):
      dirs.append(os.path.join(dirpath, file))
    else:
      files.append(os.path.join(dirpath, file))
  return sortSoftware(dirs,mask),files
#-------------------------------------------------------------------------------
# Sort the names of files according to version number or text
# Only takes into consideration the name and not the filepath
def sortSoftware(files,mask):
  if len(mask)>0:
    files.sort(key=lambda s: list(map(int,filter(None,re.split(mask,os.path.basename(s))))))
  else:
    files.sort(key=lambda s: list(os.path.basename(s)))
  return files
#-------------------------------------------------------------------------------
# Write keywords from keywords.yml to beginning of markdown file
def writeKeywords(software,fp):
  if not os.path.isfile(os.path.join(SOFTWARE_DIR, software, "keywords.yaml")):
    return
  fp.write("---\n")
  fp.write("title: Information about %s\n" % (software))
  fp.write("keywords:\n")
  with open(os.path.join(SOFTWARE_DIR, software, "keywords.yaml"), 'r') as file:
    yaml_data = yaml.safe_load(file)
  for value in yaml_data['keywords']:
    fp.write("  - %s\n" % (value))
  fp.write("---\n")
#-------------------------------------------------------------------------------
# Check if software is installed on active clusters
def checkSoftware(softwarename):
  found=False
  if not os.path.isfile(os.path.join(SOFTWARE_DIR, softwarename, "versions.yaml")):
    return found
  with open(os.path.join(SOFTWARE_DIR, softwarename, "versions.yaml"), 'r') as file:
    yaml_data = yaml.safe_load(file)
  if yaml_data is None:
    return found
  if "resources" not in yaml_data:
    return found
  for resource in yaml_data['resources']:
    if CLUSTERS.get(resource['resource'],"")!="":
      found=True
  return found
#-------------------------------------------------------------------------------
# Write which versions of the software are installed
def writeVersions(softwarename,fp,fpidx):
  with open(os.path.join(SOFTWARE_DIR, softwarename, "versions.yaml"), 'r') as file:
    yaml_data = yaml.safe_load(file)
  fp.write("\n## Installed versions\n\n")
  fp.write("| Resource | Version |\n|---|---|\n")
  fpidx.write("| [%s](%s) | " % (softwarename.capitalize(),os.path.join(softwarename,"index.md")))
  firstidx=True
  for resource in yaml_data['resources']:
    cluster=CLUSTERS.get(resource['resource'],"")
    if cluster=="":
      continue
    if not firstidx:
      fpidx.write("|| ")
    firstidx=False
    fp.write("| %s/%s | " % (cluster,resource['resource']))
    fpidx.write("%s/%s | " % (cluster,resource['resource']))
    if isinstance(resource['versions'], list):
      versionname=[]
      for version_info in resource['versions']:
        versionname.append(str(version_info['version']))
      fp.write(", ".join(versionname))
      fpidx.write(", ".join(versionname))
    fpidx.write(" |\n")
    fp.write(" |\n")
  fp.write("\n")
#-------------------------------------------------------------------------------
# Write general information about the software
def appendGeneralInfo(softwarename,fp):
  fp2=open(os.path.join(SOFTWARE_DIR,softwarename,"general.md"),"r")
  fp.write("## General information\n\n")
  for line in fp2:
    fp.write(line)
  fp2.close()
  fp.write("\n")
#-------------------------------------------------------------------------------
def main():
  os.system("rm -rf %s/*" % (SOFTWARE_DOCS))
  os.system("cp %s/template/mkdocs.yml %s" % (SOFTWARE_MAIN,SOFTWARE_MAIN))
  os.system("cp %s/template/index.md %s" % (SOFTWARE_MAIN,SOFTWARE_DOCS))
  os.system("cp -r %s/template/static %s" % (SOFTWARE_MAIN,SOFTWARE_DOCS))
  softwares,files=getDirectoryList(SOFTWARE_DIR,'')
  fpyml=open(SOFTWARE_MAIN+"/mkdocs.yml","a")
  fpidx=open(SOFTWARE_DOCS+"/index.md","a")
  for software in softwares:
    softwarename=os.path.basename(software)
    if not checkSoftware(softwarename):
      continue
    os.system("mkdir -p %s" % (os.path.join(SOFTWARE_DOCS,softwarename)))
    file=os.path.join(SOFTWARE_DOCS,softwarename,"index.md")
    fpyml.write("  - %s: %s\n" % (softwarename.capitalize(),os.path.join(softwarename,"index.md")))
    fp=open(file,"w")
    writeKeywords(softwarename,fp)
    fp.write("# %s\n" % (softwarename.capitalize()))
    writeVersions(softwarename,fp,fpidx)
    appendGeneralInfo(softwarename,fp)
    fp.close()
  fpyml.close()
  fpidx.close()
#-------------------------------------------------------------------------------
if __name__ == '__main__':
  main()
