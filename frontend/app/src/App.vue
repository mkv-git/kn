<template>
  <div id="app" class="container">
  <EasyDataTable
    buttons-pagination
    alternating
    border-cell
    :rows-per-page="10"
    :headers="headers"
    :items="items"
  >
    <template #item-operation="item">
      <div class="operation-wrapper">
        <img
          src="./images/delete.png"
          class="operation-icon"
          @click="deleteItem(item)"
        />
        <img
          src="./images/edit.png"
          class="operation-icon"
          @click="editItem(item)"
        />
      </div>
    </template>
  </EasyDataTable>
  </div>
</template>

<script lang='ts'>
  import axios from 'axios';
  import type { Header, Item } from "vue3-easy-data-table";
  import { defineComponent } from 'vue';

	export default defineComponent({
    name: 'App',
    data() {
      const items: Items[] = [];
      const headers: Header[] = [
        {text: "Name", value: "s_name"},
        {text: "Start timestamp", value: "s_start_ts"},
        {text: "End timestamp", value: "s_end_ts"},
        {text: "From", value: "s_from"},
        {text: "To", value: "s_to"},
        {text: "Finished", value: "s_done"},
        {text: "Operation", value: "operation"},
      ];

      return {
        headers: headers,
        items: items,
      }
    },
    mounted() {
      this.loadData();
    },
    methods: {
      loadData() {
        axios
          .get('http://127.0.0.1:8000/api/shipments/')
          .then((response) => {
              this.items = response.data.results;
          })
          .catch((e) => {
            console.log(e);
          });
      },
      editItem(item: Item){
      },
      deleteItem(item: Item){
        axios
          .delete('http://127.0.0.1:8000/api/shipments/' + item.id + '/')
          .then((response) => {
            console.log(response);
        })
        .catch((e) => {
          console.log(e);
        });
      }
    }
  })
</script>

<style>
.operation-wrapper .operation-icon {
  width: 20px;
  cursor: pointer;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
}      
</style>
