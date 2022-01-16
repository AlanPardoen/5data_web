<template>
  <div class="graphs">
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=84fa524d-f45f-4645-9574-84914496b8b6&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=fc278cc2-d23d-4b36-9de2-e8aec6eb96f5&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=435da782-72b9-405c-8858-f71b356b6c4b&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=b5563111-5033-4541-adc4-50e9de24b439&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=eef8953c-4aac-4a2b-90aa-259a4a636db7&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=ac5184d2-5351-48fa-a9b8-56b953fa32c2&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=5f2410be-de31-4be2-bd73-960c70054929&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=1812f58d-b782-4756-a43f-84f1025ef183&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=c8296082-0890-4c7f-ba6e-aa01467a5f0c&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=5ae222f6-5801-4ada-a641-db93f6e445b9&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=b7dfb6c8-07fb-4f9e-82e6-df3f7d24550d&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=7a0095fa-4670-46a9-bf7a-2ca47cec2ad2&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
    <iframe  src="https://charts.mongodb.com/charts-5data-czjwi/embed/charts?id=4175b52f-b2cb-49b0-aaca-9d15d7260c7e&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Graphs',
  components: { 
  },
  data() {
    return {
      graphs: [
        {name:"Pie", link:"https://charts.mongodb.com/charts-5data-czjwi/public/dashboards/61e34040-8fae-4ede-8cad-c52dd6019f4f"},
        {name:"Ligne", link:"https://s2.qwant.com/thumbr/0x380/d/9/484842ba3e437a26af664a599626ccf8d269aa00ec7dbb24612dd23c1d9474/line-graph.png?u=https%3A%2F%2Fwww.math-only-math.com%2Fimages%2Fline-graph.png&q=0&b=1&p=0&a=0"},
        {name:"Col", link:"https://s1.qwant.com/thumbr/0x380/a/f/73e7d946d023b50b5a9b68ecef6a14d30e061d3847769dd1f503050ceb330b/featured.png?u=https%3A%2F%2Fdominicroye.github.io%2Fen%2F2018%2Fthe-pie-chart%2Ffeatured.png&q=0&b=1&p=0&a=0"},
      ]
    }
  }
}
</script>
<style scoped>
  iframe{
    width:640px; 
    height:480px;
    background: #ffffff;
    border: none;
    border-radius: 2px;
    box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);

  }
</style>