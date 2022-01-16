<template>
  <div class="home">
    <h1>Campus</h1>
  <div class="location-contain">
    <div class="locations" v-for="location in locations" :key="location.name">
      <div class="Place">
        <img :src="location.img" />
        <h1>{{ location.name }}</h1>
        <h2>{{ location.desc }}</h2>
        <h2>{{ location.croi }}</h2>
    </div>
  </div>
  </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Home',
  components: { 
  },
  methods:{
      GetCampusData(name){
        axios
            .get('http://127.0.0.1:5000/campusdata?campusname='+name)
            .then(response => {
              this.locations.forEach(element => {
                if (element.name == name) {
                  element.desc =  response.data
                }
               });
            })
        axios
            .get('http://127.0.0.1:5000/growrate?campusname='+name)
            .then(response => {
              this.locations.forEach(element => {
                if (element.name == name) {
                  element.croi =  response.data
                }
               });
            })
      }
  },
  data() {
    return {
      locations: [
        {
          name: 'Lyon',
          img: 'https://www.wallpapertip.com/wmimgs/39-390850_aberdeen-university-campus.jpg',
          desc: 'loading ...',
          croi:'loading ...'
        },
        {
          name: 'Caen',
          img: 'https://jourdelaterre.org/wp-content/uploads/2018/11/make_your_campus_green_jour_de_la_terre_france.png',
          desc: 'loading ...',
          croi:'loading ...'
        },
         {
          name: 'Tours',
          img: 'https://business.ladn.eu/wp-content/uploads/2021/09/wework-lance-growth-campus-europe-startup.jpg',
          desc: 'loading ...',
          croi:'loading ...'
        },
         {
          name: 'Paris',
          img: 'https://u-paris.fr/wp-content/uploads/2019/03/vie-de-campus.png',
          desc: 'loading ...',
          croi:'loading ...'
        },
         {
          name: 'Lille',
          img: 'https://www.lea-cfi.fr/sites/default/files/styles/1366x650/public/2020-10/bandeau-campus-LEA-orly-1920x1080.jpg?itok=6zMVxRzN',
          desc:'loading ...',
          croi:'loading ...'
        },
      ]
    }
  },
  mounted() {
    this.GetCampusData("Lyon");
    this.GetCampusData("Caen");
    this.GetCampusData("Tours");
    this.GetCampusData("Paris");
    this.GetCampusData("Lille");
  }

}
</script>
<style scoped>
  body {
  width: 100vw;
  height: 100vh;
  font-family: 'NTR', sans-serif;
  background: #eee;
}

h1 {
  text-align: center;
}

.locations{
  padding: 10px;
  width: 45%;
  display: inline-block;

}

.place {
  justify-content: center;
  background: white;
  border: 1px solid #ddd;
  padding: 20px 20px;
}
h2
{
  margin: 0;
  text-align: center;
}
img {
  max-width: 40%;
  height: auto;
}

</style>
