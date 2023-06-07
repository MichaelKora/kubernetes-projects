web_content = """<!DOCTYPE html>
<html>
<body>

<h1>Kubernetes Pods</h1>
<p>Init pattern</p>

Init containers are exactly like regular containers, except:

Init containers always run to completion.
Each init container must complete successfully before the next one starts.
If a Pod's init container fails, the kubelet repeatedly restarts that init container until it succeeds. However, if the Pod has a restartPolicy of Never, and an init container fails during startup of that Pod, Kubernetes treats the overall Pod as failed.

Because init containers have separate images from app containers, they have some advantages for start-up related code:

Init containers can contain utilities or custom code for setup that are not present in an app image. 
For example, there is no need to make an image FROM another image just to use a tool like sed, awk, python, or dig during setup.
The application image builder and deployer roles can work independently without the need to jointly build a single app image.
Init containers can run with a different view of the filesystem than app containers in the same Pod. Consequently, they can be given access to Secrets that app containers cannot access.
Because init containers run to completion before any app containers start, init containers offer a mechanism to block or delay app container startup until a set of preconditions are met. 
Once preconditions are met, all of the app containers in a Pod can start in parallel.
Init containers can securely run utilities or custom code that would otherwise make an app container image less secure. By keeping unnecessary tools separate you can limit the attack surface of your app container image.

</body>
</html>
"""
file_name = "/app/index.html"
# file_name = "index.html"
text_file = open(file_name, "w")
text_file.write(web_content)
text_file.close()

file1 = open(file_name, mode='r')
content = file1.read()
print(content)
file1.close()