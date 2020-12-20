<template>
  <div>
    <a-divider>
      <h3>社團清單</h3>
    </a-divider>
    <a-row type="flex" justify="center" align="top">
      <a-col :span="22">
        <a-tabs default-active-key="1" @change="callback">
          <a-tab-pane key="1" tab="我管理的社團">
            <a-list item-layout="horizontal" :data-source="manage">
              <a-list-item slot="renderItem" slot-scope="item">
                <a-list-item-meta description="一些簡介">
                  <router-link slot="title" :to="{ name: 'manage', params: { id: item.id } }">{{ item.title }}</router-link>
                  <a-avatar
                    slot="avatar"
                    src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                  />
                </a-list-item-meta>
              </a-list-item>
            </a-list>
          </a-tab-pane>
          <a-tab-pane key="2" tab="我加入的社團">
            <a-list item-layout="horizontal" :data-source="join">
              <a-list-item slot="renderItem" slot-scope="item">
                <a-list-item-meta description="一些簡介">
                  <router-link slot="title" :to="{ name: 'announce', params: { id: item.id } }">{{ item.title }}</router-link>
                  <a-avatar
                    slot="avatar"
                    src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                  />
                </a-list-item-meta>
              </a-list-item>
            </a-list>
          </a-tab-pane>
          <a-tab-pane key="3" tab="所有社團">
            <a-collapse @change="callback">
              <a-collapse-panel key="1" header="學術性社團">
                <a-list item-layout="horizontal" :data-source="clubs.academic">
                  <a-list-item slot="renderItem" slot-scope="item">
                    <a-list-item-meta description="一些簡介">
                      <router-link slot="title" :to="{ name: 'announce', params: { id: item.id } }">{{ item.title }}</router-link>
                      <a-avatar
                        slot="avatar"
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                      />
                    </a-list-item-meta>
                  </a-list-item>
                </a-list>
              </a-collapse-panel>
              <a-collapse-panel key="2" header="體育性社團" :disabled="false">
                <a-list item-layout="horizontal" :data-source="clubs.physical">
                  <a-list-item slot="renderItem" slot-scope="item">
                    <a-list-item-meta description="一些簡介">
<router-link slot="title" :to="{ name: 'announce', params: { id: item.id } }">{{ item.title }}</router-link>                      <a-avatar
                        slot="avatar"
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                      />
                    </a-list-item-meta>
                  </a-list-item>
                </a-list>
              </a-collapse-panel>
              <a-collapse-panel key="3" header="學生自治">
                <a-list item-layout="horizontal" :data-source="clubs.student">
                  <a-list-item slot="renderItem" slot-scope="item">
                    <a-list-item-meta description="一些簡介">
<router-link slot="title" :to="{ name: 'announce', params: { id: item.id } }">{{ item.title }}</router-link>                      <a-avatar
                        slot="avatar"
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                      />
                    </a-list-item-meta>
                  </a-list-item>
                </a-list>
              </a-collapse-panel>
            </a-collapse>
          </a-tab-pane>
        </a-tabs>
      </a-col>
    </a-row>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Home',
  data () {
    return {
      manage: [
        {
          id: '1',
          title: '資訊研習社',
        }
      ],
      join: [
        {
          id: '2',
          title: '滔滔社',
        },
        {
          id: '3',
          title: '映画社'
        }
      ],
      clubs: {
        academic: [
          {
            title: '資訊研習社',
          },
          {
            title: '滔滔社',
          }
        ],
        physical: [
          {
            title: '排球社'
          },
          {
            title: '羽球社'
          }
        ],
        student: [
          {
            title: '學生會',
          },
          {
            title: '學生議會'
          }
        ]
      }
    }
  },
  mounted () {

  },
  methods: {
    callback(key) {
      console.log(key);
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  font-weight: bold;
}
</style>
