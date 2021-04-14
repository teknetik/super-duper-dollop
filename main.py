import kong

httpbin = kong.Service("httpbin")

print(httpbin.Route.delete('anything'))
if httpbin.exists:
    print("Exists, Attemping to delete")
    print(httpbin.delete())

create = httpbin.create("http", "httpbin.org", "80", "/anything")

print("Created a host pointing to upstream host of " + str(create['host']))

print("The " + httpbin.name + " service is using the protocol " + httpbin.protocol)

print(httpbin.Route("httpbin").add(name="anything", paths="/anything", methods="GET", tags="test-tag", hosts="httpbin.org"))



for i in range(500, 999):
    value = str(i)
    print(httpbin.Route("httpbin").add(name=value, paths="/" + value, methods="GET", tags=["test-tag", "another-tag"]))
for i in range(1000, 1500):
    value = str(i)
    print(httpbin.Route("httpbin").add(name=value, paths="/" + value, methods="GET", tags="provision"))
