def call(Closure other_job, String domain) {
    node {
        stage("Hello World") {
            script {
                sh """
                    echo Hello
                """
                echo "${domain}"
            }
        }
        other_job()
    }
}
