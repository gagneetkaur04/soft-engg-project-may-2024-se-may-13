<template>
  <div class="card border-dark mb-3">
    <div class="nav-item text-nowrap card-header d-flex justify-content-center" @click="toggleFlag">
      <div>
        <a class="text-center text-decoration-none dropdown-toggle" aria-expanded="false">
          <strong>week - {{ weekNumber }}</strong>
        </a>
      </div>
    </div>
    <div v-if="flag">
      <div class="card-body">
        <div class="nav-item text-wrap" v-for="(value, key) in weekContents">
          <a class="align-items-center text-decoration-none pt-1 pb-1 " aria-expanded="false"
            :href="`/course/${courseId}?contentId=${value.content_id}`">
            <span style=" font-size: 1rem;">{{ value.lecture_title }}</span>
          </a>
          <hr width="100%" top="0" bottom="0" p-0 m-0>
        </div>
        <div class="nav-item text-wrap p-1" v-if="assignmentType == 'MCQ'">
          <a class="align-items-center text-decoration-none" aria-expanded="false"
            :href="`/course/${courseId}?assignmentId=${assignment[0].assignments[0].assignment_id}&weekNumber=${assignment[0].week_number}`">
            <span style="font-size: 1rem;">assignment - {{ assignment[0].week_number }}</span>
          </a>
        </div>
        <div class="nav-item text-wrap p-1" v-else>
          <a class="align-items-center text-decoration-none" aria-expanded="false"
            :href="`/course/${courseId}?progAssignmentId=${assignment[0].prog_assignment_id}`">
            <span style="font-size: 1rem;">programming assignment - {{ assignment[0].prog_assignment_id }}</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'SideNavItem',
  data: function () {
    return {
      flag: false,
    }
  },
  props: {
    courseId: String,
    courseTitle: String,
    weekNumber: Number,
    weekContents: Array,
    assignment: Array,
    assignmentType: String,
  },
  methods: {
    toggleFlag() {
      this.flag = !this.flag;
    }
  }
}
</script>
<style>
a:hover {
  text-decoration: none;
  background-color: none;
}
</style>
