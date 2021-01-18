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
                  <router-link slot="title" :to="{ name: 'manage', params: { id: item.id } }">{{ item.name }}</router-link>
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
                  <router-link slot="title" :to="{ name: 'announce', params: { id: item.id } }">{{ item.name }}</router-link>
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
              <a-collapse-panel key="1" header="自治組織">
                <a-list item-layout="horizontal" :data-source="clubs['自治組織']">
                  <a-list-item slot="renderItem" slot-scope="item">
                    <a-list-item-meta description="一些簡介">
                      <router-link slot="title" :to="{ name: 'announce', params: { id: item.id } }">{{ item.name }}</router-link>
                      <a-avatar
                        slot="avatar"
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                      />
                    </a-list-item-meta>
                  </a-list-item>
                </a-list>
              </a-collapse-panel>
              <a-collapse-panel key="2" header="系學會委員會">
                <a-list item-layout="horizontal" :data-source="clubs['系學會委員會']">
                  <a-list-item slot="renderItem" slot-scope="item">
                    <a-list-item-meta description="一些簡介">
                      <router-link slot="title" :to="{ name: 'announce', params: { id: item.id } }">{{ item.name }}</router-link>
                      <a-avatar
                        slot="avatar"
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                      />
                    </a-list-item-meta>
                  </a-list-item>
                </a-list>
              </a-collapse-panel>
              <a-collapse-panel key="3" header="服務性委員會">
                <a-list item-layout="horizontal" :data-source="clubs['服務性委員會']">
                  <a-list-item slot="renderItem" slot-scope="item">
                    <a-list-item-meta description="一些簡介">
                      <router-link slot="title" :to="{ name: 'announce', params: { id: item.id } }">{{ item.name }}</router-link>
                      <a-avatar
                        slot="avatar"
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                      />
                    </a-list-item-meta>
                  </a-list-item>
                </a-list>
              </a-collapse-panel>
              <a-collapse-panel key="4" header="學術性委員會">
                <a-list item-layout="horizontal" :data-source="clubs['學術性委員會']">
                  <a-list-item slot="renderItem" slot-scope="item">
                    <a-list-item-meta description="一些簡介">
                      <router-link slot="title" :to="{ name: 'announce', params: { id: item.id } }">{{ item.name }}</router-link>
                      <a-avatar
                        slot="avatar"
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                      />
                    </a-list-item-meta>
                  </a-list-item>
                </a-list>
              </a-collapse-panel>
              <a-collapse-panel key="5" header="康樂性委員會">
                <a-list item-layout="horizontal" :data-source="clubs['康樂性委員會']">
                  <a-list-item slot="renderItem" slot-scope="item">
                    <a-list-item-meta description="一些簡介">
                      <router-link slot="title" :to="{ name: 'announce', params: { id: item.id } }">{{ item.name }}</router-link>
                      <a-avatar
                        slot="avatar"
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                      />
                    </a-list-item-meta>
                  </a-list-item>
                </a-list>
              </a-collapse-panel>
              <a-collapse-panel key="6" header="體育性委員會">
                <a-list item-layout="horizontal" :data-source="clubs['體育性委員會']">
                  <a-list-item slot="renderItem" slot-scope="item">
                    <a-list-item-meta description="一些簡介">
                      <router-link slot="title" :to="{ name: 'announce', params: { id: item.id } }">{{ item.name }}</router-link>
                      <a-avatar
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
      manage: [],
      join: [],
      clubs: {}
    }
  },
  mounted () {
    this.getClubs()
  },
  methods: {
    getClubs () {
      this.axios.get(
        '/club'
      ).then((response) => {
        console.log(response.data)
        let clubs = response.data.clubs
        this.manage = clubs.manage
        this.join = clubs.join
        this.clubs = clubs.clubs
        console.log(this.manage)
        console.log(this.join)
        console.log(this.clubs)
      })
    },
    callback (key) {
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
