# debug-jaeger-tracing
Test program to debug Jaegertracing on OpenShift

# Deploy

## Add or set project

    oc login -u <username> -p <password>

    # either create new project
    oc new-project tracetest --display-name="Trace testing"
    
    # or set project existing  
    oc project tracetest 

## Add new app (once) 

OpenShift add new app from source

    oc new-app c:\dev\debug-jaeger-tracing

or from github

    oc new-app https://github.com/josteinl/debug-jaeger-tracing

## Expose port 5000

    oc expose svc/debug-jaeger-tracing


# References

https://scoutapm.com/blog/tutorial-tracing-python-flask-requests-with-opentracing
