def call(String domain, Integer code) {
    return {
        stage("check website code ${domain}") {
            script {
                response_code = sh (
                    script: "curl -o /dev/null -s -w %{http_code} ${domain}",
                    returnStdout: true
                ).toInteger()

                echo "${response_code}"   
            }
        }
        stage ("Check response code") {
            steps{
                script{
                    if ( response_code != code ){
                        sh "false"
                    }             
                }

            }
        }        
    }
}



