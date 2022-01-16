<template>
  <div class="data">
    <table id="firstTable">
      <thead>
          <tr>
              <th v-for="(col, index) in columns" :key="index">{{col}}</th>
          </tr>
      </thead>
      <tbody>
          <tr v-for="(user, index) in users" :key="index">
             <td v-for="(col, index) in columns" :key="index">{{user[col]}}</td>
          </tr>
      </tbody>
    </table> 
  </div>
</template>
<script>
import axios from 'axios'
  export default {
    name: 'Data',
    components: { 
    },
    data() {
      return {
        users: [
          
        ],
        tables_names:[]
      }
    },
    mounted () {
          axios
            .get('http://127.0.0.1:5000/data?table=Student')
            .then(response => {this.users = response.data})
    },
  computed: {
    "columns": function columns() {
      if (this.users.length == 0) {
        return [];
      }
      return Object.keys(this.users[0])
    }
    }
  }
</script>
<style scoped>

  table {
    font-family: 'Open Sans', sans-serif;
    border-collapse: collapse;
    border: 3px solid #44475C;
    margin: 5px;
  }
  table th {
    text-transform: uppercase;
    text-align: left;
    background: #44475C;
    color: #FFF;
    padding: 5px;
    min-width: 10px;
  }
  table td {
    text-align: left;
    padding: 5px;
    border-right: 2px solid #7D82A8;
  }
  table td:last-child {
    border-right: none;
  }
  table tbody tr:nth-child(2n) td {
    background: #D4D8F9;
  }
</style>