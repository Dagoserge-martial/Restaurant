new Vue({
    el: '#test',
    data: {
        url: 'http://127.0.0.1:8000/service/',
        info: null
    },
    mounted () {
        //getServiceMenu() {
        axios
          .get('http://127.0.0.1:8000/service/?format=json')
          .then(response => {this.info = response})
          .catch(error=>{console.log(error)}
          )
        //}
        
    }
    
})