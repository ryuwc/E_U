

<template>
    
    <div class="flex justify-start p-1 mt-3 ml-4">
    <ul>
        <!-- Validate Email -->
        <li x-show="formData.email.length > 0" class="flex items-center py-1">
            <div 
              :class="{'bg-green-200 text-green-700': isEmail(formData.email),
               'bg-red-200 text-red-700': !isEmail(formData.email)}"
                class="p-1 rounded-full fill-current ">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" 
                  stroke="currentColor">
                    <path
                        x-show="isEmail(formData.email)"
                        stroke-linecap="round" stroke-linejoin="round" 
                        stroke-width="2" d="M5 13l4 4L19 7" />
                    <path
                        x-show="!isEmail(formData.email)"
                        stroke-linecap="round" stroke-linejoin="round" 
                        stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </div>
            <span
                :class="{'text-green-700': isEmail(formData.email), 
                  'text-red-700': !isEmail(formData.email)}"
                class="ml-3 text-sm font-medium"
                x-text="isEmail(formData.email) ? 
                'Email is valid' : 'Email is not valid!' "></span>
        </li>
       
        <!-- Validate Password -->
        <li x-show="formData.password.length > 0" class="flex items-center py-1">
            <div 
              :class="{'bg-green-200 text-green-700': formData.password.length > 7,
              'bg-red-200 text-red-700':formData.password.length < 8 }"
                class="p-1 rounded-full fill-current ">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path 
                      x-show="formData.password.length > 7" stroke-linecap="round"
                      stroke-linejoin="round" 
                      stroke-width="2" d="M5 13l4 4L19 7" />
                    <path x-show="formData.password.length < 8" 
                      stroke-linecap="round" stroke-linejoin="round" 
                      stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </div>

            <span
                :class="{'text-green-700': formData.password.length > 7, 
                'text-red-700':formData.password.length < 8 }"
                class="ml-3 text-sm font-medium"
                x-text="formData.password.length > 7 ? 
                'The minimum length is reached' : 
                'At least 8 characters required' "></span>
        </li>
        
        <!-- Validate Password Confirm -->
        <li x-show="formData.password_confirm > 0" class="flex items-center py-1">
            <div 
              :class="{'bg-green-200 text-green-700': 
              formData.password === formData.password_confirm, 
              'bg-red-200 text-red-700':formData.password !== 
              formData.password_confirm}"
                class="p-1 rounded-full fill-current ">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path
                        x-show="formData.password === formData.password_confirm"
                        stroke-linecap="round" stroke-linejoin="round" 
                        stroke-width="2" d="M5 13l4 4L19 7" />
                    <path
                        x-show="formData.password !== formData.password_confirm"
                        stroke-linecap="round" stroke-linejoin="round" 
                        stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </div>

            <span
                :class="{'text-green-700': 
                formData.password === formData.password_confirm, 
                'text-red-700':formData.password !== formData.password_confirm}"
                class="ml-3 text-sm font-medium"
                x-text="formData.password === formData.password_confirm ? 
                'Passwords match' : 'Passwords do not match' "></span>
        </li>

    </ul>
</div>

</template>



<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.js" defer></script>
<script>
export default {
  name: "FinalPjtFrontTestView",

  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style scoped></style>
