from client import Job

# this where we actually invoke the tests
print("Always-pass test....."),
alwaysdef = {"DockerJob":{"image": "always_pass"}}
alwayspass = Job(alwaysdef)
result = alwayspass.execute()
print result

print("Always-fail test....."),
alwaysfaildef = {"DockerJob":{"image": "always_fail"}}
alwaysfail = Job(alwaysfaildef)
result = alwaysfail.execute()
print result

print("Testing APIC Login..."),
passjobref = {"DockerJob": {"image":"apic-api-test"}}
passjob = Job(passjobref)
result = passjob.execute()
print result


# container aborts - python import failure
print("Testing bad plugin....."),
failedjobdef = {"DockerJob": {"image":"plugintest"}}
failedjob = Job(failedjobdef)
result = failedjob.execute()
print result

# this is an invalid plugin, it does not provide JSON data back
print("invalid plugin - not providing JSON back...."),
failedjob1 = {"DockerJob": {"image":"hello-world"}}
failedjob1 = Job(failedjob1)
result = failedjob1.execute()
print result
# works

print("toolkit lint...."),
realfailuredef = {"DockerJob": {"image":"apic-acitoolkit-lint"}}
realfailure = Job(realfailuredef)
result = realfailure.execute()
print result

print("testing plugin not found..."),
notfoundjobdef = {"DockerJob": {"image":"dslkfj"}}
notfoundjob = Job(notfoundjobdef)
result = notfoundjob.execute()
print result.json()
print result
