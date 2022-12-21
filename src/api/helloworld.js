import request from "../utils/requests";

export function getmsg(params) {
  return request({
    url: `/api`,
    method: 'get',
    params
  })
}
