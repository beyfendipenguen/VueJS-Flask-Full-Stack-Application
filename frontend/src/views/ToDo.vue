<template>
  <div class="jumbotron vertical-center">
    <!-- bootswatch CDN -->
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
      integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
      crossorigin="anonymous"
    />

    <div class="container"> 
      <div class="row">
        <div class="col-sm-12">
          <h1 class="text-center bg-primary text-white" style="border-radius: 10px"> TO-DO-List 📋</h1>
          <hr />
          <br />

          <!-- Alert Message -->
          <b-alert variant="success" v-if="showMessage"
            :show="dismissCountDown"
            dismissible
            @dismissed="dismissCountDown=0"
            @dismiss-count-down="countDownChanged"
          >{{ message }}</b-alert>

          <!-- Add new task button -->
          <button class="btn btn-success bt-sm" v-b-modal.add-task-modal>Add Task</button>
          <hr />
          <br />
          
          <!-- Start table -->
          <table class="table table-hover">
            <!-- Table Head -->
            <thead>
              <tr>
                <!-- Table header cells -->
                <th scope="col">Task</th>
                <th scope="col">Status</th>
                <th scope="col">Priority</th>
                <th scope="col">Due date</th>
                <th scope="col">Assignee</th>
                <th scope="col">Notes</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <!-- Table Body -->
            <tbody>
              <tr v-for="(task, index) in tasks" :key="index">
                <!-- td : table data  -->
                <td>{{ task.task }}</td>
                <td>
                  <span v-if="task.status">Completed &#10004;</span>
                  <span v-else>Uncompleted &#10006;</span>
                </td>
                <td>
                  <span v-if="task.priority.toLocaleLowerCase() === 'high'" style="background-color: #ff3333; border-radius: 3px; font-size: 15px">High</span>
                  <span v-else style="background-color: #c6ff1a; border-radius: 5px; font-size: 15px">Low</span>
                </td>
                <td>{{ task.due_date }}</td>
                <td>{{ task.assignee }}</td>
                <td>{{ task.notes }}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info btn-sm" v-b-modal.update-task-modal @click="editTask(task)">
                      Update
                    </button>
                    <button type="button" class="btn btn-danger btn-sm" @click="deleteTask(task)">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <!-- End table -->

          <!-- Start footer -->
          <footer class="bg-primary text-white text-center" style="border-radius: 10px">
            Copyright &copy; All Rights Reserved 2021 To-Do-List.
          </footer>
          <!-- End footer -->

        </div>
      </div>

      <!-- Start add task modal  -->
      <b-modal ref="AddTaskModal" id="add-task-modal" title="Add new task" hide-backdrop hide-footer>
        <b-form class="w-100" @submit="onSubmit" @onreset="onReset">

          <b-form-group id="form-tesk-group" label="Task:" label-for="form-task-input">
            <b-form-input 
              id="form-task-input"
              type="text"
              v-model="addTaskForm.task"
              required
              placeholder="Enter task*"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-priority-group" label="Priority:" label-for="form-priority-input">
            <b-form-input
              id="form-priority-input"
              type="text"
              v-model="addTaskForm.priority"
              required
              placeholder="Priority*"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-due_date-group" label="Due date:" label-for="form-Due_date-input">
            <b-form-input
              id="form-due_date-input"
              type="text"
              v-model="addTaskForm.due_date"
              required
              placeholder="Due date*"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-assignee-group" label="assignee" label-for="form-assignee-input">
            <b-form-input
              id="form-assignee-input"
              type="text"
              v-model="addTaskForm.assignee"
              required
              placeholder="Assignee*"
            > 
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-notes-group" label="notes" label-for="form-notes-input">
            <b-form-input
              id="form-notes-input"
              type="text"
              v-model="addTaskForm.notes"
              placeholder="Notes"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-status-group">
            <b-form-checkbox-group
              v-model="addTaskForm.status"
              id="form-checks"
            >
              <b-form-checkbox value="true">Completed?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>          

          <b-button type="submit" variant="outline-info">Submit</b-button>
          <b-button type="reset" variant="outline-danger">Reset</b-button>
        </b-form>
      </b-modal>
      <!-- End add task modal  -->

      <!-- Start edit task modal -->
      <b-modal ref="EditTaskModal" id="update-task-modal" title="Update task" hide-backdrop hide-footer>
        <b-form class="w-100" @submit="onSubmitUpdate" @reset="onResetUpdate">

          <b-form-group id="form-tesk-group" label="Task:" label-for="form-task-edit-input">
            <b-form-input 
              id="form-task-edit-input"
              type="text"
              v-model="editForm.task"
              required
              placeholder="Enter task*"
            >
            </b-form-input>
          </b-form-group>         

          <b-form-group id="form-priority-group" label="Priority:" label-for="form-priority-edit-input">
            <b-form-input
              id="form-priority-edit-input"
              type="text"
              v-model="editForm.priority"
              required
              placeholder="Priority*"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-due_date-group" label="Due date:" label-for="form-Due_date-edit-input">
            <b-form-input
              id="form-due_date-edit-input"
              type="text"
              v-model="editForm.due_date"
              required
              placeholder="Due date*"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-assignee-group" label="assignee" label-for="form-assignee-edit-input">
            <b-form-input
              id="form-assignee-edit-input"
              type="text"
              v-model="editForm.assignee"
              required
              placeholder="Assignee*"
            > 
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-notes-group" label="notes" label-for="form-notes-edit-input">
            <b-form-input
              id="form-notes-edit-input"
              type="text"
              v-model="editForm.notes"
              placeholder="Notes"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-status-edit-group">
            <b-form-checkbox-group
              v-model="editForm.status"
              id="form-checks"
            >
              <b-form-checkbox value="true">Completed?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>   

          <b-button-group>
            <b-button type="submit" variant="outline-info">Update</b-button>
            <b-button type="reset" variant="outline-danger">Cancel</b-button>
          </b-button-group>

        </b-form>
      </b-modal>
      <!-- End edit task modal -->

    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      tasks: [],
      addTaskForm: {
        task: '', 
        status: [],
        priority: '', 
        due_date: '',
        assignee: '',
        notes: ''
      },
      editForm: {
        id: '',
        status: [],
        priority: '', 
        due_date: '',
        assignee: '',
        notes: ''
      },
      message: "",
      showMessage: false,
      dismissSecs: 5,
      dismissCountDown: 0,
    };
  },
  methods: {
    // Add new task modal functions
    // Get Function 
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
      .then((response) => {
        this.tasks = response.data.Tasks;
      })
      .catch((error) => {
        console.error(error);
      });
    },
    // Post Function
    addTask(payloed) {
      const path = 'http://localhost:5000/task';
      axios.post(path, payloed)
      .then(() => {
        this.getTasks();
        this.message = "Task added 📋 !";
        this.showMessage = true;
        this.showAlert();
      })
      .catch((error) => {
        console.error(error);
        this.getTasks();
      });
    },
    // Init form
    initForm() {
      // Add task data
      this.addTaskForm.task = '';
      this.addTaskForm.status = '';
      this.addTaskForm.priority = '';
      this.addTaskForm.due_date = '';
      this.addTaskForm.assignee = '';
      this.addTaskForm.notes = '';
      // Edit task data
      this.editForm.id = '';
      this.editForm.task = '';
      this.editForm.status = '';
      this.editForm.priority = '';
      this.editForm.due_date = '';
      this.editForm.assignee = '';
      this.editForm.notes = '';
    },
    onSubmit(e) {
      e.preventDefault();
      this.$refs.AddTaskModal.hide();
      let status = false;
      if (this.addTaskForm.status[0]) status = true;
      const payloed = {
        task: this.addTaskForm.task,
        status: status,
        priority: this.addTaskForm.priority,
        due_date: this.addTaskForm.due_date,
        assignee: this.addTaskForm.assignee,
        notes: this.addTaskForm.notes,
      };
      this.addTask(payloed);
      this.initForm();
    },
    onReset(e) {
      e.preventDefault();
      this.$refs.AddTaskModal.hide();
      this.initForm();
    },
    // Edit task modal functions
    // On submit update
    onSubmitUpdate(e) {
      e.preventDefault();
      this.$refs.EditTaskModal.hide();
      let status = false;
      if (this.editForm.status[0]) status = true;
      const payloed = {
        id: this.editForm.id,
        task: this.editForm.task,
        status: status,
        priority: this.editForm.priority,
        due_date: this.editForm.due_date,
        assignee: this.editForm.assignee,
        notes: this.editForm.notes,
      };
      this.updateTask(payloed, this.editForm.id);
    },
    // Update task
    updateTask(payloed, taskId) {
      const path = `http://localhost:5000/task/${taskId}`;
      axios.put(path, payloed)
      .then(() => {
        this.getTasks();
        this.message = 'Task updated ⚙️!';
        this.showMessage = true;
        this.showAlert();
      })
      .catch((error) => {
        console.error(error);
        this.getTasks();
      });
    },
    editTask(task) {
      this.editForm = task;
    }, 
    // Handle reset / cancel button click
    onResetUpdate(e) {
      e.preventDefault();
      this.$refs.EditTaskModal.hide();
      this.initForm();
      this.getTasks();
    },
    // Handle  detete button
    removeTask(taskId) {
      const path = `http://localhost:5000/task/${taskId}`;
      axios.delete(path)
      .then(() => {
        this.getTasks();
        this.message = 'Task Removed 🗑️!';
        this.showMessage = true;
        this.showAlert();
      })
      .catch((error) => {
        console.error(error);
        this.getTasks();
      });
    },
    deleteTask(task) {
      this.removeTask(task.id);
    },
    // Handle  alert message
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs
    },

  },
  created() {
    this.getTasks();
  },
};
</script>
