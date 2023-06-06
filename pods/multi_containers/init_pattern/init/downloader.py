web_content = """<h1>Kubernetes multi containers pod</h1>
<h2>Init container</h2>
<p style="font-size: 1.5em;"> <strong style="background-color: #317399; padding: 0 5px; color: #fff;">Init Containers</strong>  are containers that run before the main container runs with your containerized application. They normally contain setup scripts that prepares an environment for you containerized application. Init Containers also ensure the wider server environment is ready for your application to start to run.</p>

"""
file_name = "/app/index.html"
text_file = open(file_name, "w")
text_file.write(web_content)
text_file.close()
